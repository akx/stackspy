# -- encoding: utf-8 --
from __future__ import with_statement
import re

def detect_django_admin(context):
	url = context.get_url("/admin/")
	if "__admin_media_prefix__" in url.content:
		url.add_result("Django", "Django admin media prefix")

def detect_django_csrf_middleware(context):
	for url in context.html_urls:
		if "name='csrfmiddlewaretoken'" in url.content:
			url.add_result("Django", "Django CSRF middleware token")

EASYTHUMBNAILS_RE = re.compile("\.jpg\.\d+x\d+_q\d+\.jpg$", re.I)

def detect_django_easythumbnails(context):
	for url in context.html_urls:
		if url.html_tree is not None:
			for img_tag in url.html_tree.findall("*/img"):
				src = img_tag.get("src")
				if EASYTHUMBNAILS_RE.search(src):
					url.add_result("django-easythumbnails", "Thumbnail URL match", detail=src)

def detect_django_csrftoken(context):
	for url in context.html_urls:
		cookie = url.headers.get("Set-Cookie") or ""
		if re.search('csrftoken=[a-zA-Z0-9]+', cookie):
			url.add_result("Django", "Django CSRF token cookie")