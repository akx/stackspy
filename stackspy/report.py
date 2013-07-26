# -- encoding: utf-8 --
from __future__ import with_statement


class Report(object):
	def __init__(self, context):
		self.context = context

	def write_text(self, stream):
		print >>stream, "# Report for base URL %s" % self.context.base_url
		print >>stream
		print >>stream, "%d URLs requested" % len([1 for u in self.context.all_urls if u.requested])
		print >>stream

		for url_ctx in self.context.all_urls:
			if url_ctx.exists:
				if url_ctx.results or url_ctx.status_code != 200:
					print >>stream, "## %s" % url_ctx.url
					print >>stream


					if url_ctx.status_code != 200:
						print >>stream, "Status: %d" % url_ctx.status_code

					if url_ctx.redirected:
						print >>stream, "Request was redirected to: %s" % url_ctx.redirected

					if url_ctx.results:
						print >>stream
						for result in url_ctx.results:
							print >>stream, "* %s" % unicode(result)
							if result.detail:
								print >>stream, "  %s" % unicode(result.detail)
						print >>stream