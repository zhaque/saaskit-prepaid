from django.conf import settings

ITEM_PREFIX = getattr(settings, 'PREPAID_ITEM_PREFIX', 'P')
UNIT_COST = getattr(settings, 'PREPAID_UNIT_COST', .1)

MIN_WITHDRAWAL = getattr(settings, 'PREPAID_MIN_WITHDRAWAL', 10)

ROOT_URL = getattr(settings, 'ROOT_URL')

RECHARGE_TEXT = 'Point Purchase'

PREPAID_UNIT_PACKS = getattr(settings, 'PREPAID_UNIT_PACKS', (
	(10, '1.29'),
	(100, '12.49'),
	(250, '29.99'),
	(500, '57.99'),
	(1000, '109.99'),
))
