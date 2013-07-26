# -- encoding: utf-8 --
from __future__ import with_statement


class Result(object):
	def __init__(self, url_ctx, group, description=None, detail=None, confidence=0.7):
		self.url_ctx = url_ctx
		self.group = group
		self.description = description
		self.detail = detail
		self.confidence = confidence

	def __unicode__(self):
		return "%s: %s" % (self.group, self.description)