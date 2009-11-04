from django.conf import settings

ITEM_PREFIX = getattr(settings, 'PREPAID_ITEM_PREFIX', 'P-')
UNIT_COST = getattr(settings, 'PREPAID_UNIT_COST', 1)

ROOT_URL = getattr(settings, 'ROOT_URL')
