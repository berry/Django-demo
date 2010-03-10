from django.conf.urls.defaults import *

urlpatterns = patterns('djangodemo.subjecten.views',
    (r'^$', 'index'),
    (r'^(?P<subject_id>\d+)/$', 'detail'),
	(r'^(?P<subject_id>\d+)/edit/$', 'edit'),
	(r'^(?P<subject_id>\d+)/wijzig/$', 'edit'),
    (r'^nieuw/$', 'new'),
    (r'^new/$', 'new'),
)