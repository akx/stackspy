# -- encoding: utf-8 --
from __future__ import with_statement

def detect_aspnet(context):
	for url in context.html_urls:
		if url.html_tree is not None and url.html_tree.cssselect('#__VIEWSTATE'):
			url.add_result("ASP.net", "Viewstate formfield")
		if url.sets_cookie("NET_SessionId"):
			url.add_result("ASP.net", "Session ID cookie")