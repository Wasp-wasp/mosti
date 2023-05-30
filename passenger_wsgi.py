# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/www/prometheus.ru/mosti/data/www/faq-reg.ru/project_name')
sys.path.insert(1, '/var/www/www/prometheus.ru/mosti/data/djangoenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mosti.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()