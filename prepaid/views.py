from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .util import render_to
from .models import UnitPack
from .conf import *

from paypal.standard.forms import PayPalPaymentsForm

def _get_point_buy_form(username, points, next = None):
	if not next:
		next = 'prepaid-index'
	paypal_dict = {
		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'amount': '%s' % (points * UNIT_COST),
		'item_name': 'Points', #'%s Points' % points,
		'item_number': ITEM_PREFIX, #'%s%s' % (ITEM_PREFIX, points),
		'custom':str(username),
		#'invoice': 'unique-invoice-id',
		'notify_url': ROOT_URL + reverse('paypal-ipn'),
		'return_url': ROOT_URL + reverse(next),
		'cancel_return': ROOT_URL + reverse('prepaid-index'),
	}

	# Create the instance.
	return PayPalPaymentsForm(initial=paypal_dict)

@login_required
@render_to('prepaid/points.html')
def points(request):
	next = request.GET.get('next')
	
	point_form = _get_point_buy_form(request.user.username, 0, next=next)
	
	points = UnitPack.get_user_credits(request.user)
	
	return {'points':points, 'point_form':point_form, 'packs':PREPAID_UNIT_PACKS}
