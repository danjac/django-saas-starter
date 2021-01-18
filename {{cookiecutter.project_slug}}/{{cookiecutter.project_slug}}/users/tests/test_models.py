# Third Party Libraries
import pytest

# Local
from ..factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserManager:
    def test_create_user(self, user_model):

        user = user_model.objects.create_user(
            username="tester", email="tester@gmail.com", password="t3ZtP4s31"
        )
        assert user.check_password("t3ZtP4s31")

    def test_create_superuser(self, user_model):

        user = user_model.objects.create_superuser(
            username="tester", email="tester@gmail.com", password="t3ZtP4s31"
        )
        assert user.is_superuser
        assert user.is_staff

    def test_matches_usernames(self, user_model):
        user_1 = UserFactory(username="first")
        user_2 = UserFactory(username="second")
        user_3 = UserFactory(username="third")

        names = ["second", "FIRST", "SEconD"]  # duplicate

        users = user_model.objects.matches_usernames(names)
        assert len(users) == 2
        assert user_1 in users
        assert user_2 in users
        assert user_3 not in users

        # check empty set returns no results
        assert user_model.objects.matches_usernames([]).count() == 0
