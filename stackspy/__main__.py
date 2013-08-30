# -- encoding: utf-8 --
from __future__ import with_statement
import sys
import time
from werkzeug.utils import secure_filename

try:
	from stackspy.context import Context
except ImportError:
	import os
	sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))
	from stackspy.context import Context

import logging
import argparse

def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("url")
	ap.add_argument("-v", action="store_true", default=False, dest="verbose", help="be verbose")
	ap.add_argument("-d", action="store_true", default=False, dest="debug", help="show debug")
	ap.add_argument("-u", default=None, dest="user_agent", help="change user agent")
	ap.add_argument("-a", default=None, dest="archive", help="Save request/response archive")
	args = ap.parse_args()
	if args.verbose:
		logging.basicConfig(level=logging.INFO)
	elif args.debug:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.ERROR)
	context = Context(base_url=args.url, debug=args.debug, user_agent=args.user_agent)
	context.run_all_detectors()
	report = context.generate_report()
	report.write_text(sys.stdout)
	if args.archive:
		args.archive += "_%d" % time.time()
		context.create_archive(args.archive)





if __name__ == "__main__":
	main()