# -- encoding: utf-8 --
from __future__ import with_statement
from collections import  OrderedDict
import cookielib
import urlparse
from requests import Request
from requests.cookies import cookiejar_from_dict, RequestsCookieJar
from requests.structures import CaseInsensitiveDict
from requests.utils import to_key_val_list


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

def merge_setting_safe(request_setting, session_setting, dict_class=OrderedDict):
	merged_setting = dict_class(to_key_val_list(session_setting or ()))
	merged_setting.update(to_key_val_list(request_setting or ()))
	for (k, v) in (request_setting or {}).items():
		if v is None:
			del merged_setting[k]
	return merged_setting


def create_request(session, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None):
	cookies = cookies or {}

	if not isinstance(cookies, cookielib.CookieJar):
		cookies = cookiejar_from_dict(cookies)

	merged_cookies = RequestsCookieJar()
	merged_cookies.update(session.cookies)
	merged_cookies.update(cookies)
	cookies = merged_cookies

	params = merge_setting_safe(params, session.params)
	headers = merge_setting_safe(headers, session.headers, dict_class=CaseInsensitiveDict)
	auth = merge_setting_safe(auth, session.auth)

	return Request(method=method.upper(), url=url, headers=headers, files=files, data=data, params=params, auth=auth, cookies=cookies)