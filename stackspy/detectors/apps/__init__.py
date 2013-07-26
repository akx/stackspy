# -- encoding: utf-8 --
from __future__ import with_statement
from stackspy.detection.utils import find_in_html_by_substring, find_all_linked_css


def detect_magento(context):
	find_in_html_by_substring(context, {
		"varien/js.js": ("Magento", "Varien Javascript library")
	})

def detect_zencart(context):
	find_in_html_by_substring(context, {
		"shopping cart program by Zen Cart": ("Zen Cart", "Zen Cart generator tag")
	})

def detect_oscommerce(context):
	find_in_html_by_substring(context, {
		"/shopping_cart.php": {"group": "osCommerce", "description": "shopping_cart.php", "confidence": 0.2},
		'Powered by <a href="http://www.oscommerce.com" target="_blank">osCommerce</a>': ("osCommerce", "Powered by osCommerce tag"),
	})

def detect_wordpress(context):
	for css_url in find_all_linked_css(context, local_only=True):
		if "wp-content/themes/" in css_url:
			context.add_url(css_url).add_result("WordPress", "wp-content theme URL")

def detect_joomla(context):
	find_in_html_by_substring(context, {
		"Joomla! 1.5 -": ("Joomla", "Joomla 1.5 tag"),
		"/components/com_": ("Joomla", "Joomla component URL format"),
	})