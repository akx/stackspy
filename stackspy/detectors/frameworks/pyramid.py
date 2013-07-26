# -- encoding: utf-8 --
from __future__ import with_statement
from stackspy.utils import first
import difflib



def probe_pyramid_no_slashes(context):
	test_url = first(u.url for u in context.html_urls if len(u.relative_url) > 2 and u.endswith("/"))
	if test_url:
		with_slash = context.get_url(test_url)
		without_slash = context.get_url(test_url.rstrip("/"))
		if difflib.get_close_matches(with_slash.content, [without_slash.content], 1, 0.8) != []:
			test_url.add_result("Pyramid", "Don't care about slashes behavior", detail="Tested against %s" % without_slash.url, confidence=0.3)