# -- encoding: utf-8 --
from __future__ import with_statement

def detect_ror_auth_token(context):
	for url in context.html_urls:
		if '<meta content="authenticity_token"' in url.content:
			url.add_result("Ruby on Rails", "Authenticity Token meta-tag")

def detect_ror_application_js(context):
	for url in context.html_urls:
		if 'src="/javascripts/application.js?' in url.content:
			url.add_result("Ruby on Rails", "javascripts/application.js")