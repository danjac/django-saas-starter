import contextlib

from django.core.exceptions import PermissionDenied


def has_perm_or_403(user, permission, obj=None):
    if not user.has_perm(permission, obj):
        raise PermissionDenied


@contextlib.contextmanager
def handle_form(request, form_class, **form_kwargs):
    if "_request" in form_kwargs:
        form_kwargs["request"] = form_kwargs.pop("_request")
    if request.method == "POST":
        form = form_class(data=request.POST, files=request.FILES, **form_kwargs)
        yield form, form.is_valid()
    else:
        yield form_class(**form_kwargs), False
