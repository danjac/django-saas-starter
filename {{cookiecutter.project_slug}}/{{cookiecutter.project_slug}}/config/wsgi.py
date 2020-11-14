# Standard Library
import os

# Django
from django.core.wsgi import get_wsgi_application  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_slug }}.config.settings.local")

application = get_wsgi_application()
