# Copyright (c) 2020 by Dan Jacob
# SPDX-License-Identifier: AGPL-3.0-or-later

# Local
from .base import *  # noqa
from .base import ALLOWED_HOSTS

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

ALLOWED_HOSTS += [".example.com"]

CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}

THUMBNAIL_KVSTORE = "sorl.thumbnail.kvstores.cached_db_kvstore.KVStore"

SITE_ID = 1
