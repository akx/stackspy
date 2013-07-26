# -- encoding: utf-8 --
from __future__ import with_statement
import re

PHP_EXT_RE = re.compile("\.p(html|hp)[345]?$")

def detect_php_x_powered_by(context):
	for url in context.html_urls:
		xpb = url.headers.get('x-powered-by', '')
		if xpb.startswith('PHP/'):
			url.add_result("PHP", "X-Powered-By: %r" % xpb)

def detect_php_credits(context):
	url = context.get_url(context.base_url + "?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000")
	if "PHP Credits" in url.content:
		url.add_result("PHP", "PHP Credits easter egg")

def detect_php_logo(context):
	url = context.get_url(context.base_url + "?=PHPE9568F34-D428-11d2-A769-00AA001ACF42")
	if url.exists and "/gif" in url.headers.get("content-type", ""):
		url.add_result("PHP", "PHP Logo GUID")

def detect_php_extension(context):
	for url in context.local_urls:
		m = PHP_EXT_RE.match(url.url)
		if m:
			url.add_result("PHP", "PHP extension in URL", detail=m.group(0))
		if url.is_html and url.html_tree is not None:
			for link in url.html_tree.findall("*/a"):
				href = link.get("href")
				if href and PHP_EXT_RE.match(href) and context.base_url in href:
					url.add_result("PHP", "PHP extension in local link", detail=href)