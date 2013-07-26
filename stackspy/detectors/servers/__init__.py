# -- encoding: utf-8 --
from __future__ import with_statement

def detect_nginx(context):
	for url in context.all_urls:
		if "nginx" in url.headers.get("Server", "").lower():
			url.add_result("Nginx", "Server header: %r" % url.headers["Server"])

def detect_apache(context):
	for url in context.all_urls:
		if "apache" in url.headers.get("Server", "").lower():
			url.add_result("Apache", "Server header: %r" % url.headers["Server"])

def detect_iis(context):
	for url in context.all_urls:
		if "microsoft-iis" in url.headers.get("Server", "").lower():
			url.add_result("IIS", "Server header: %r" % url.headers["Server"])

