# -- encoding: utf-8 --
from __future__ import with_statement
from stackspy.utils import url_replace


def detect_robots(context):
	robots = context.get_url(url_replace(context.base_url, path="/robots.txt"))
	if robots.exists:
		robots.add_result("Robots.txt", "Robots.txt exists")

def detect_humans(context):
	humans = context.get_url(url_replace(context.base_url, path="/humans.txt"))
	if humans.exists:
		humans.add_result("Humans.txt", "Humans.txt exists")