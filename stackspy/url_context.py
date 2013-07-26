# -- encoding: utf-8 --
from __future__ import with_statement
import requests
from stackspy.result import Result
import logging

try:
	from lxml.html import document_fromstring
except ImportError:
	document_fromstring = None


log = logging.getLogger(__name__)

class FailedResponse(object):
	status_code = -500
	content = ""
	headers = {}
	def __init__(self, url):
		self.url = url

class UrlContext(object):
	def __init__(self, context, url):
		self.context = context
		self.url = url
		self.is_local = bool(url.startswith(context.base_url))
		self.relative_url = url.replace(context.base_url, "")  # XXX: This isn't really bullet-proof at all
		self.results = []
		self.redirected = False
		self._request = None
		self._response = None
		self._html_tree = None

	@property
	def requested(self):
		return (self._request and self._response)

	@property
	def request(self):
		if self._request is None:
			self._request = requests.Request("GET", self.url)
		return self._request

	@property
	def response(self):
		if self._response is None:
			log.info("%r Requesting: %r", self, self.url)
			try:
				self._response = self.context.session.send(self.request.prepare())
			except:
				log.exception("Couldn't request URL %r" % self.url)
				self._response = FailedResponse(self.url)

			if self.url != self._response.url:
				log.info("%r ended up in a redirect to %r." % (self.url, self._response.url))
				self.redirected = self._response.url

			if self.status_code != 200:
				log.info("%r status: %d", self.url, self.status_code)

		return self._response

	@property
	def headers(self):
		return self.response.headers

	@property
	def content(self):
		return self.response.content

	@property
	def exists(self):
		return (self.response.status_code != 404)

	@property
	def is_html(self):
		return ("html" in self.headers.get("content-type")) or ("<html" in self.content.lower())

	@property
	def status_code(self):
		return self.response.status_code

	@property
	def html_tree(self):
		if self._html_tree is None:
			if document_fromstring:
				self._html_tree = document_fromstring(self.content)
				self._html_tree.make_links_absolute(self.url)
		return self._html_tree

	def add_result(self, group, description="", detail=None, confidence=0.7):
		self.results.append(Result(self, group=group, description=description, detail=detail, confidence=confidence))

	def sets_cookie(self, cookie_name):
		return ("; %s=" % cookie_name) in self.headers.get("set-cookie", "")
