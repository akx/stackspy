# -- encoding: utf-8 --
from __future__ import with_statement
from importlib import import_module
import os

class Detector(object):
	def __init__(self):
		pass

	def detect(self, context):
		raise NotImplementedError("Not implemented")

	def __call__(self, context):
		return self.detect(context)




def find_all_modules(base_path):
	for dirpath, dirnames, filenames in os.walk(base_path):
		for filename in filenames:
			if filename.endswith(".py"):
				filename = os.path.normpath(os.path.join(dirpath, filename))
				yield filename


def find_all_detectors():
	base_path = os.path.dirname(__file__)
	for module_filename in find_all_modules(base_path):
		module_imp = "stackspy.detectors.%s" % os.path.splitext(module_filename.replace(base_path, ""))[0].replace(os.path.sep, ".").strip(".")
		module = import_module(module_imp)
		for name, obj in vars(module).iteritems():

			if name.startswith("detect") and callable(obj):
				yield obj

			try:
				if not issubclass(obj, Detector) or obj is Detector:
					continue
			except TypeError:
				continue

			yield obj()
