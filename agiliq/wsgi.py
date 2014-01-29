"""
WSGI config for agiliq project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agiliq.settings")

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD
#application = get_wsgi_application()

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
=======
application = get_wsgi_application()
>>>>>>> aa7865c040a4e75aa975090edd1ffdede996c183
