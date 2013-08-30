# -- encoding: utf-8 --
from __future__ import with_statement
import re

def detect_spring_security(context):
	for url in context.html_urls:
		if url.html_tree is not None:
			for input_tag in url.html_tree.findall("*/input"):
				if input_tag.get("name", "").startswith("spring-security"):
					url.add_result("Spring", "Spring Security form field", detail=input_tag.get("name"))
