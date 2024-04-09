# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2586156/data/www/manningimp/manningproj')
sys.path.insert(1, '/var/www/u2586156/data/manningvenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'manningproj.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
