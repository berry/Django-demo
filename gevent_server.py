import os
import sys

PORTNUMBER = 8088
DJANGO_DIR = '/Users/berry/Django-1.1.1/'
PROJECT_DIR_NAME = 'djangodemo'

# use insert instead of append to make sure that 
# the directory is searched first.
# This prevents that a potential django directory within the
# python/site-packages is searched first.
sys.path.insert(0, DJANGO_DIR)
# also insert current projectdirectory and go on directory up
sys.path.insert(0, os.sep.join((os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])))

os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % PROJECT_DIR_NAME

from gevent import monkey; monkey.patch_all() # see: http://www.gevent.org/
from gevent import wsgi
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

print "Starting Gevent server on port: %s" % PORTNUMBER
wsgi.WSGIServer(('', PORTNUMBER), application).serve_forever()
