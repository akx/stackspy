# -- encoding: utf-8 --
from __future__ import with_statement
import urlparse

def detect_drupal(context):
	for url in context.local_urls:
		for meta in url.html_tree.findall("*/meta"):
			if meta.get("name") == "generator" and "Drupal" in (meta.get("content") or ""):
				url.add_result("Drupal", "Drupal generator metatag", detail=meta.get("content"))
		if urlparse.urlparse(url.url).path.startswith("/sites/default/"):
			url.add_result("Drupal", "/sites/default/ in URL")