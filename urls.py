from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("django.views.generic.simple",
	
	# Hoofdpagina's
	(r'^$', "direct_to_template", {'template': 'index.html'}),
)

urlpatterns = urlpatterns + patterns('',
    # Example:
    # (r'^djangodemo/', include('djangodemo.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # Subjecten
    (r'^subjecten/', include("djangodemo.subjecten.urls")),
    
    # Static media
    # ONLY USE THIS FOR THE DEVELOPMENT SERVER. NEVER USE THIS IN PRODUCTION.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/berry/git/djangodemo/static'}),
)
