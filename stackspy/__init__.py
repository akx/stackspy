# -- encoding: utf-8 --
from __future__ import with_statement
from stackspy.context import Context


def spy(url):
	context = Context(base_url=url)
	context.run_all_detectors()
	return context.generate_report()