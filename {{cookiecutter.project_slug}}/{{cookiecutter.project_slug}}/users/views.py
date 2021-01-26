# Standard Library
import datetime

# Django
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.http import require_POST
from turbo_response import TurboStream, redirect_303, render_form_response

from {{cookiecutter.project_slug}}.shortcuts import handle_form

from .forms import UserCreationForm


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request):
    redirect_url = get_redirect_url(request) or settings.LOGIN_REDIRECT_URL
    if request.user.is_authenticated:
        return redirect(redirect_url)

    with handle_form(request, AuthenticationForm, _request=request) as (
        form,
        is_success,
    ):
        if is_success:
            auth_login(request, form.get_user())
            return redirect_303(redirect_url)

        return render_form_response(
            request, form, "account/login.html",
            {
                "redirect_field_name": REDIRECT_FIELD_NAME,
                "redirect_field_value": redirect_url,
            },

        )


@sensitive_post_parameters()
@csrf_protect
@never_cache
def signup(request):
    with handle_form(request, UserCreationForm) as (form, is_success):
        if is_success:
            form.save()
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            auth_login(request, user)
            return redirect_303(settings.LOGIN_REDIRECT_URL)
        return render_form_response(request, form, "account/signup.html")


@require_POST
@never_cache
def logout(request):
    auth_logout(request)
    return redirect(get_redirect_url(request) or settings.LOGOUT_REDIRECT_URL)


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


def get_redirect_url(request):
    redirect_to = request.POST.get(
        REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME, "")
    )
    if redirect_to and url_has_allowed_host_and_scheme(
        url=redirect_to,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return redirect_to
    return None
