import datetime

from django.conf import settings
from django.contrib import auth
from django.db import models
from .conf import *
from decimal import Decimal

from paypal.standard.ipn.signals import payment_was_successful
from django.http import QueryDict
	
def receive_point_buy(sender, **kwargs):
	# FIXME: handle errors?
	ipn = sender
		
	if ipn.item_number == ITEM_PREFIX:
		query = QueryDict(ipn.query)
		quantity = int(query['option_selection1'])
		for units, price in PREPAID_UNIT_PACKS:
			if quantity == units:
				if ipn.mc_gross == Decimal(price):
					user = auth.models.User.objects.get(username=ipn.custom)
					UnitPack.credit(user, quantity, reason=RECHARGE_TEXT)
				break
payment_was_successful.connect(receive_point_buy)

class ValidUnitPackManager(models.Manager):
	def get_query_set(self):
		return super(ValidUnitPackManager, self).get_query_set().filter(
			expires__gt=datetime.date.today(), quantity__gt=0)

def _default_expires():
	if hasattr(settings,'PREPAID_DEFAULT_EXPIRY_PERIOD'):
		return datetime.date.today() + datetime.timedelta(
			settings.PREPAID_DEFAULT_EXPIRY_PERIOD)

class UnitPack(models.Model):
	# Normally we only deal with not expired and not empty unit packs,
	# but sometimes we need to peek into expired.
	all_objects = models.Manager()
	objects = ValidUnitPackManager()

	user = models.ForeignKey(auth.models.User)
	quantity = models.IntegerField()
	expires = models.DateField(default=_default_expires)

	# bookkeeping
	timestamp = models.DateTimeField(auto_now_add=True)
	initial_quantity = models.IntegerField()

	class Meta:
		ordering = ('expires',)

	def is_valid(self):
		return self.quantity>0 and self.expires>datetime.date.today()
	is_valid.boolean = True

	@classmethod
	def get_user_packs(cls, user):
		return cls.objects.filter(user=user)

	@classmethod
	def get_user_credits(cls, user):
		return sum(up.quantity for up in cls.get_user_packs(user))
		
	@classmethod
	def credit(cls, user, quantity=1, reason=''):
		up = UnitPack()
		up.user = user
		up.quantity = quantity
		up.save()
		
		t = Transaction()
		t.user = user
		t.info = reason
		t.amount = quantity
		t.total = cls.get_user_credits(user)
		t.credit = True
		t.save()

	@classmethod
	def consume(cls, user, quantity=1, reason=''):
		q_total = quantity
		ups = cls.get_user_packs(user)
		if sum(up.quantity for up in ups) < quantity:
			raise ValueError("User does not have enough units.")
		for up in ups:
			if up.quantity >= quantity:
				up.quantity -= quantity
				up.save()
				break
			quantity -= up.quantity
			up.quantity = 0
			up.save()
		
		t = Transaction()
		t.user = user
		t.info = reason
		t.amount = q_total
		t.total = cls.get_user_credits(user)
		t.save()
			
class Transaction(models.Model):
	user = models.ForeignKey(auth.models.User, related_name='prepaid_transactions')
	date = models.DateTimeField(auto_now_add=True)
	amount = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
	credit = models.BooleanField(default=False)
	info = models.CharField(max_length=300)
	
	def __unicode__(self):
		return self.info
	
	class Meta:
		ordering = ['-date']

# provide default value for initial_quantity
def _handle_pre_save(sender, instance=None, **kwargs):
	assert instance is not None
	if instance.pk is None and instance.initial_quantity is None:
		instance.initial_quantity = instance.quantity
models.signals.pre_save.connect(_handle_pre_save, sender=UnitPack)

#
