from django.conf.urls.defaults import *

from djangodemo.zaken.models import Zaak

# create/update/delete van zaken
# nieuwe zaak wordt aangemaakt via /subjecten/{{ id }}/zaken/new/
urlpatterns = patterns('djangodemo.zaken.views',
	(r'^(?P<zaak_id>\d+)/(edit|wijzig)/$', 'edit'),
)

# list/detail van zaken
zaken = Zaak.objects.select_related().all()

urlpatterns += patterns('django.views.generic.list_detail',
    (r'^$',             'object_list', {
		'queryset': zaken,
		'template_name': 'zaken/index.html',
		'template_object_name': 'zaak',
		'paginate_by': 25}),
    (r'^(?P<object_id>\d+)/$', 'object_detail', {
		'queryset': zaken,
		'template_name': 'zaken/detail.html', 
		'template_object_name': 'zaak'}),
)

