# Standard Library
import datetime

# Django
from django.utils import timezone
from django.views.decorators.http import require_POST

from turbo.response import TurboStream


@require_POST
def accept_cookies(request):
    response = TurboStream("accept-cookies").remove.response()
    response.set_cookie(
        "accept-cookies",
        value="true",
        expires=timezone.now() + datetime.timedelta(days=30),
        samesite="Lax",
    )
    return response
