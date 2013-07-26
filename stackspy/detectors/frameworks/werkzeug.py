# -- encoding: utf-8 --
from __future__ import with_statement

def detect_werkzeug_easter_egg(context):
	url = context.get_url(context.base_url + '?macgybarchakku')
	if url.status_code == 200 and 'the Swiss Army knife of Python web development' in url.content:
		url.add_result("Werkzeug", "Werkzeug easter egg")