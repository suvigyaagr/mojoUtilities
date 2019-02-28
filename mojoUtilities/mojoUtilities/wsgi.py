"""
WSGI config for mojoUtilities project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/shreyaskm/mojoUtilities/mojoUtilities'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mojoUtilities.settings'


from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mojoUtilities.settings")

application = get_wsgi_application()
