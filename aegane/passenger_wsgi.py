# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, 'C:/Users/nikita/web/aegane/aegane')
sys.path.insert(1, 'C:/Users/nikita/AppData/Local/Programs/Python/Python311/Lib/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'aegane.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()