from django.conf.urls.defaults import *

urlpatterns = patterns('djangodemo.subjecten.views',
    (r'^$', 'index'),
    (r'^(?P<subject_id>\d+)/$', 'detail'),
)