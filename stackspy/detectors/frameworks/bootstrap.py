# -- encoding: utf-8 --
from __future__ import with_statement
import re
from stackspy.detection.utils import find_all_linked_js

BOOTSTRAP_CSS_RE = re.compile("bootstrap[a-z0-9.-_]+\.css", re.I)
BOOTSTRAP_JS_RE = re.compile("bootstrap[a-z0-9.-_]+\.js", re.I)

def detect_bootstrap(context):
	for url in context.all_urls:
		m = BOOTSTRAP_CSS_RE.search(url.content)
		if m:
			url.add_result("Bootstrap", "Bootstrap CSS", detail=m.group(0))
		m = BOOTSTRAP_JS_RE.search(url.content)
		if m:
			url.add_result("Bootstrap", "Bootstrap JS", detail=m.group(0))
	for js_url, referrers in find_all_linked_js(context).iteritems():
		js = context.get_url(js_url)
		if "Bootstrap.js by" in js.content:
			js.add_result("Bootstrap.js")