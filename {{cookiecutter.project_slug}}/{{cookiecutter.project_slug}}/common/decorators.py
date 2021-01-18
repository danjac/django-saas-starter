import functools
import json

# Django
from django.contrib.messages.api import get_messages


def add_messages_to_response_header(view):
    """Takes messages added to request, moves them to JSON in http header"""

    @functools.wraps(view)
    def wrapper(request, *args, **kwargs):
        response = view(request, *args, **kwargs)
        # do not apply to redirects
        if getattr(response, "url", None) is None:
            messages = [
                {"message": str(message), "tags": message.tags}
                for message in get_messages(request)
            ]
            response["X-Messages"] = json.dumps(messages)
        return response

    return wrapper
