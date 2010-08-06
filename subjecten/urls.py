from django.conf.urls.defaults import *

from djangodemo.zaken.models import Zaak
from djangodemo.subjecten.models import Subject

# list/detail van subjecten
subjecten = Subject.objects.select_related().all()
urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', {
		'queryset': subjecten,
		'template_name': 'subjecten/index.html',
		'template_object_name': 'subject',
		'paginate_by': 3}),
    (r'^(?P<object_id>\d+)/$', 'object_detail', {
		'queryset': subjecten,
		'template_name': 'subjecten/detail.html', 
		'template_object_name': 'subject'}),
)

# CRUD pagina's subjecten en zaak functies bij subject
urlpatterns += patterns('djangodemo.subjecten.views',
    (r'^new/$', 'new'),
	(r'^(?P<subject_id>\d+)/(edit|wijzig)/$', 'edit'),
	(r'^(?P<subject_id>\d+)/zaken/$', 'zaken'),
	(r'^(?P<subject_id>\d+)/zaken/(new|nieuw)/$', 'new_zaak_for_subject'),
)
