# -- encoding: utf-8 --
from __future__ import with_statement
import re
from stackspy.detection.utils import find_all_linked_js

JQUERY_RE = re.compile("jquery[a-z0-9.-_]+\.js", re.I)

def detect_jquery(context):
	for url in context.all_urls:
		m = JQUERY_RE.search(url.content)
		if m:
			url.add_result("jQuery", "jQuery JS", detail=m.group(0))
	for js_url, referrers in find_all_linked_js(context).iteritems():
		js = context.get_url(js_url)
		if not (js_url.endswith("jquery.js") or js_url.endswith("jquery.min.js")):
			if "jQuery JavaScript Library" in js.content:
				js.add_result("jQuery", "jQuery JS")