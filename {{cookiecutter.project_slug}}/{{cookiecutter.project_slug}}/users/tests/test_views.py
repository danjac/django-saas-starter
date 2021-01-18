import pytest
import http

from django.urls import reverse
from django.conf import settings

pytestmark = pytest.mark.django_db


class TestLogin:
    def test_post_login_invalid(self, client):
        resp = client.post(
            reverse("account_login"), {"username": "user", "password": "wrong"}
        )
        assert resp.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY

    def test_post_login_valid(self, client, user, password):
        resp = client.post(
            reverse("account_login"), {"username": "user", "password": password}
        )
        assert resp.url == settings.LOGIN_REDIRECT_URL

    def test_get(self, client):
        resp = client.get(reverse("account_login"))
        assert resp.status_code == http.HTTPStatus.OK

    def test_get_if_authenticated(self, client, login_user):
        resp = client.get(reverse("account_login"))
        assert resp.url == settings.LOGIN_REDIRECT_URL


class TestSignup:
    def test_get(self, client):
        resp = client.get(reverse("account_signup"))
        assert resp.status_code == http.HTTPStatus.OK

    def test_post_login_valid(self, client, user_model):
        resp = client.post(
            reverse("account_signup"),
            {"username": "user", "password1": "testpass1", "password2": "testpass1"},
        )
        assert resp.url == settings.LOGIN_REDIRECT_URL
        user = user_model.objects.get()
        assert user.username == "user"
        assert user.check_password("testpass1")


class TestLogout:
    def test_post(self, client, login_user):
        assert client.post(reverse("account_logout")).url == settings.LOGIN_REDIRECT_URL


class TestAcceptCookies:
    def test_post(self, client):
        assert client.post(reverse("accept_cookies")).status_code == http.HTTPStatus.OK
