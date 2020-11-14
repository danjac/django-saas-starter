# Local
from .base import *  # noqa
from .base.aws import *  # noqa
from .base.mailgun import *  # noqa
from .base.secure import *  # noqa

# Required for Heroku SSL
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
