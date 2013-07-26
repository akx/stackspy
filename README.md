Stackspy
========

Try to find out the underlying technology behind web sites.

Written originally as a 3-hour Explosion Friday hack project at [Anders Inno](http://www.andersinno.fi).

Usage
-----

1. Make sure you have the requirements (see requirements.txt). Mainly a fresh enough version of [Requests](http://python-requests.org/) and [Werkzeug](http://werkzeug.pocoo.org/).
   LXML is not required, but some detections won't work without it.

2. Run the script. For Python 2.7 (which is what you ought to be using anyway), you should be able to just run

    python -m stackspy http://www.google.com/

Hacking
-------

You can add your own detectors as functions that take a `stackspy.context.Context` parameter
somewhere in the `stackspy.detectors` package and the framework should automagically pick them up.

Pull requests are very welcome.

