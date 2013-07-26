# -- encoding: utf-8 --
from __future__ import with_statement
import sys
try:
	from stackspy import spy
except ImportError:
	import os
	sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))
	from stackspy import spy

import logging
import argparse

def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("url")
	ap.add_argument("-v", action="store_true", default=False, dest="verbose", help="be verbose")
	ap.add_argument("-d", action="store_true", default=False, dest="debug", help="show debug")
	args = ap.parse_args()
	if args.verbose:
		logging.basicConfig(level=logging.INFO)
	elif args.debug:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.ERROR)
	report = spy(args.url)
	report.write_text(sys.stdout)

if __name__ == "__main__":
	main()