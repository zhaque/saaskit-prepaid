from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def render_to(template=''):
	def deco(view):
		def fn(request, *args, **kargs):
			if 'template' in kargs:
				t = kargs['template']
				del kargs['template']
			else:
				t = template
			r = view(request, *args, **kargs) or {}
			if isinstance(r, HttpResponse):
				return r
			else:
				c = RequestContext(request, r)
				return render_to_response(t, context_instance=c)
		return fn
	return deco
