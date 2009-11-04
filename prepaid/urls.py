from django.conf.urls.defaults import *

urlpatterns = patterns('prepaid.views',
    (r'^$', 'get_points', {}, 'prepaid-index'),
)
