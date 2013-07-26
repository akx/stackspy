# -- encoding: utf-8 --
from __future__ import with_statement
from stackspy.detection.utils import find_all_linked_css


def detect_less(context):
	for css_url, referrers in find_all_linked_css(context, local_only=True).iteritems():
		less_url = css_url.replace("css", "less")
		if context.get_url(less_url).exists:
			context.base.add_result("Mirror LESS", "LESS counterpart found", detail={"css": css_url, "less": less_url})
		css = context.get_url(css_url)
		if "LESS Elements" in css.content:
			css.add_result("LESS Elements")

