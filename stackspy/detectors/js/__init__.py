# -- encoding: utf-8 --
from __future__ import with_statement
from stackspy.detection.utils import find_in_html_by_substring

SIMPLE_SUBSTRINGS = {
	".google-analytics.com/ga.js": "Google Analytics",
	"js/chartbeat.js": "Chartbeat",
    ".snoobi.com/snoop": "Snoobi",
	".quantserve.com/quant.js": "QuantServe",
	".addthis.com/js": "AddThis",
	"Typekit.load": "Typekit",
    "//connect.facebook.net/": "Facebook SDK",
    "platform.twitter.com/widgets.js": "Twitter Widget",
    "www.attracta.com/tb/": "Attracta Toolbar",
    "var NREUMQ=NREUMQ||[]": "New Relic End User Monitoring",
}


def detect_js(context):
	find_in_html_by_substring(context, SIMPLE_SUBSTRINGS)

