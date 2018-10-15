"""
WSGI config for parkourdex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import confy
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dot_env = os.path.join(BASE_DIR, '.env')
if os.path.exists(dot_env):
    confy.read_environment_file(dot_env)  # Must precede dj_static imports.

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parkourdex.settings')

application = get_wsgi_application()
