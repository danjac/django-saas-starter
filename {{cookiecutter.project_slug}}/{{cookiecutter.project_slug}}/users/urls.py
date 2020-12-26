# Django
from django.urls import include, path, re_path

from .views import account, socialaccount, accept_cookies

urlpatterns = [
    path("accept-cookies/", accept_cookies, name="accept_cookies"),
    path("account/login/", account.login, name="account_login"),
    path("account/signup/", account.signup, name="account_signup"),
    path(
        "account/password/change/",
        account.password_change,
        name="account_change_password",
    ),
    path(
        "account/password/set/",
        account.password_set,
        name="account_set_password",
    ),
    path(
        "account/password/reset/",
        account.password_reset,
        name="account_reset_password",
    ),
    re_path(
        r"^account/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        account.password_reset_from_key,
        name="account_reset_password_from_key",
    ),
    path(
        "account/email/",
        account.email,
        name="account_email",
    ),
    path(
        "account/social/signup/",
        socialaccount.signup,
        name="socialaccount_signup",
    ),
    path("account/", include("allauth.urls")),
]
