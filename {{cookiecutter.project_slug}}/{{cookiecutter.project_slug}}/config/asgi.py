# Standard Library
import os

from django.core.asgi import get_asgi_application  # noqa isort:skip

# django app has to be initialized first
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_slug }}.config.settings.local"
)  # noqa isort:skip

django_asgi_app = get_asgi_application()  # noqa isort:skip

from django.urls import re_path  # noqa isort:skip

from channels.routing import ProtocolTypeRouter  # noqa isort:skip


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # websocket: my_socket_app
    }
)
