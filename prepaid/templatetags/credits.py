from django import template
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.template.defaultfilters import timesince
from prepaid.models import UnitPack

register = template.Library()

@register.simple_tag
def show_user_credits(user):
	return UnitPack.get_user_credits(user)

@register.filter
def deltatime(date):
	r = timesince(date)
	if r == '0 minutes':
		return 'just now'
	else:
		return u'%s ago' % r
