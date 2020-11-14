# Copyright (c) 2020 by Dan Jacob
# SPDX-License-Identifier: AGPL-3.0-or-later

"""
WSGI config for localhub.project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

# Standard Library
import os

# Django
from django.core.wsgi import get_wsgi_application  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "localhub.config.settings.local")

application = get_wsgi_application()
