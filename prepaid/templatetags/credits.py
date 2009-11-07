from django import template
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from prepaid.models import UnitPack

register = template.Library()

@register.simple_tag
def show_user_credits(user):
	return UnitPack.get_user_credits(user)
