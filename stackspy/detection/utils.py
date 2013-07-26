# -- encoding: utf-8 --
from __future__ import with_statement
from collections import defaultdict


def find_all_linked_css(context, local_only=False):
	linked_css = defaultdict(list)
	for url in context.html_urls:
		if url.html_tree is not None:
			for link in url.html_tree.findall("*/link"):
				rel = (link.get("rel") or "").lower()
				type = (link.get("type") or "").lower()
				href = link.get("href")
				if rel == "stylesheet" or "/css" in type or ".css" in href:
					if not local_only or (local_only and href.startswith(context.base_url)):
						linked_css[href].append(url)
	return linked_css

def find_all_linked_js(context, local_only=False):
	linked_js = defaultdict(list)
	for url in context.html_urls:
		if url.html_tree is not None:
			for script in url.html_tree.findall("*/script"):
				src = script.get("src")
				if src and ".js" in src:
					if not local_only or (local_only and href.startswith(context.base_url)):
						linked_js[src].append(url)
	return linked_js

def find_in_html_by_substring(context, substrings):
	for url in context.html_urls:
		for substring, result in substrings.iteritems():
			if substring in url.content:
				if isinstance(result, basestring):
					url.add_result(result)
				elif isinstance(result, (tuple, list)):
					url.add_result(*result)
				elif isinstance(result, dict):
					url.add_result(**result)
