# -- encoding: utf-8 --
from __future__ import with_statement

def detect_grails_classpath(context):
	for url in context.local_urls:
		if "org.codehaus.groovy.grails" in url.content:
			url.add_result("Grails", "Grails classpath")
