# -- encoding: utf-8 --
from __future__ import with_statement
import urlparse
import requests
from werkzeug.urls import url_fix
from stackspy.report import Report
from stackspy.url_context import UrlContext
from stackspy.utils import is_absolute
import logging
log = logging.getLogger(__name__)



class Context(object):
	def __init__(self, base_url):
		self.base_url = base_url
		self.session = requests.Session()
		self._urls = {}
		self.base = self.get_url(base_url)

	def run_all_detectors(self):
		import stackspy.detectors as detectors
		for detector in detectors.find_all_detectors():
			detector(self)

	def generate_report(self):
		return Report(self)

	def get_url(self, url):
		if not is_absolute(url):
			log.warn("Making URL %r absolute by prepending base URL.", url)
			url = urlparse.urljoin(self.base_url, url)

		url = url_fix(url)
		url_ctx = self._urls.get(url)

		if not url_ctx:
			self._urls[url] = url_ctx = UrlContext(self, url)

		return url_ctx

	@property
	def all_urls(self):
		return self._urls.itervalues()

	@property
	def local_urls(self):
		return (url_ctx for url_ctx in self._urls.itervalues() if url_ctx.is_local)

	@property
	def html_urls(self):
		return (url_ctx for url_ctx in self._urls.itervalues() if url_ctx.is_html)