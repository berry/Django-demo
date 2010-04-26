from djangodemo.zaken.models import Zaak, Stap, Status, TypeStap, TypeStatus
from django.contrib import admin

class ZaakAdmin(admin.ModelAdmin):
	list_display = ('type_zaak', 'datum_start', 'datum_wijziging', 'subject')
	pass

admin.site.register(Zaak, ZaakAdmin)
admin.site.register(Stap)
admin.site.register(Status)
admin.site.register(TypeStap)
admin.site.register(TypeStatus)
