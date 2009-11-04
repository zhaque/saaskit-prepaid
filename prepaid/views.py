from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .util import render_to
from .models import UnitPack
from .conf import *

from paypal.standard.forms import PayPalPaymentsForm

def _get_point_buy_form(username, points):
	paypal_dict = {
		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'amount': '%s' % (points * UNIT_COST),
		'item_name': '%s Points' % points,
		'item_number': '%s%s' % (ITEM_PREFIX, points),
		'custom':str(username),
		#'invoice': 'unique-invoice-id',
		'notify_url': ROOT_URL + reverse('paypal-ipn'),
		'return_url': ROOT_URL + reverse('prepaid-index'),
		'cancel_return': ROOT_URL + reverse('prepaid-index'),
	}

	# Create the instance.
	return PayPalPaymentsForm(initial=paypal_dict)

@login_required
@render_to('prepaid/get_points.html')
def get_points(request):
	forms = []
	for i in [100, 200, 500, 1000, 5000]:
		forms.append((i, _get_point_buy_form(request.user.username, i)))
	
	points = UnitPack.get_user_credits(request.user)
	return {'points':points, 'forms': forms}
