import os, sys
sys.path.insert(0, '/home/s/b311ipv6/b311ipv6.beget.tech/public_html/HelloDjango')
sys.path.insert(1, '/home/s/b311ipv6/b311ipv6.beget.tech/venv_django/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'HelloDjango.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()