from django.conf.urls.defaults import *

urlpatterns = patterns('prepaid.views',
    (r'^$', 'points', {}, 'prepaid-index'),
)
