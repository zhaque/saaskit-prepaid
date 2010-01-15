from django.conf.urls.defaults import *

urlpatterns = patterns('prepaid.views',
    (r'^$', 'points', {}, 'prepaid-index'),
    (r'^account-summary/$', 'points', {}, 'prepaid-account-summary'),
    (r'^withdraw/$', 'withdraw', {}, 'prepaid-withdraw'),
)
