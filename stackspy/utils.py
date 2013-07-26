# -- encoding: utf-8 --
from __future__ import with_statement
import urlparse


def is_absolute(url):
	return bool(urlparse.urlparse(url).scheme)

url_key_to_index = ('scheme', 'netloc', 'path', 'params', 'query', 'fragment')


def url_replace(url, **kwargs):
	url_p = list(urlparse.urlparse(url))
	for key, value in kwargs.iteritems():
		url_p[url_key_to_index.index(key)] = value
	return urlparse.urlunparse(url_p)

def first(iterable, default=None):
	for obj in iterable:
		if obj:
			return obj
	return default