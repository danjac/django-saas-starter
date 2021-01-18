# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse

# Third Party Libraries
import pytest

from {{ cookiecutter.project_slug }}.users.factories import UserFactory


@pytest.fixture
def get_response():
    return lambda req: HttpResponse()


@pytest.fixture
def user_model():
    return get_user_model()



@pytest.fixture
def anonymous_user():
    return AnonymousUser()


@pytest.fixture
def password():
    return "testpass1"

@pytest.fixture
def user(password):
    user = UserFactory.build()
    user.set_password(password)
    user.save()
    return user


@pytest.fixture
def login_user(client, user, password):
    client.login(username=user.username, password=password)
    return user

