import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from model_bakery import baker

from users.models import User


class TestUserModels(TestCase):
    """Test User model"""

    def setUp(self) -> None:
        if isinstance(User, type):
            self.model = baker.make(User)

    def test_create_models(self):
        assert self.model


# --------------------------------------


class TestUserViews(APITestCase):
    """Teset User views"""

    def setUp(self) -> None:
        self.client = APIClient()
        # 더미 유저 생성
        self.password = "password"
        self.user = User.objects.create(
            username="kaengkaneg",
            first_name="kaeng",
            last_name="kaeng",
            email="kaengkaeng@kaengkaeng.com",
        )
        self.user.set_password(self.password)
        self.user.save()
        url = "/api/v1/users/login"
        res = self.client.post(
            url,
            json.dumps({"username": self.user.username, "password": self.password}),
            content_type="application/json",
        )
        if res is not None:
            self.http_author = f"X-JWT {res.data.get('token')}"

    def test_create_new_account(self):
        url = "/api/v1/users/"
        new_user_data = json.dumps(
            {
                "username": "kaengee",
                "first_name": "fn",
                "last_name": "ln",
                "email": "kaeng2@kaengkaeng.com",
                "password": "newpassword",
            }
        )
        res = self.client.post(url, new_user_data, content_type="application/json")
        assert res.status_code == status.HTTP_201_CREATED

    def test_login_account(self):
        url = "/api/v1/users/login"
        login_data = json.dumps({"username": self.user.username, "password": self.password})
        res = self.client.post(url, login_data, content_type="application/json")
        assert res.data.get("token") != None

    def test_get_me_success(self):
        url = "/api/v1/users/me"
        res = self.client.get(url, {}, content_type="application/json", HTTP_AUTHORIZATION=self.http_author)
        assert res.status_code == status.HTTP_200_OK

    def test_get_me_forbidden(self):
        url = "/api/v1/users/me"
        res = self.client.get(url, {}, content_type="application/json")
        assert res.status_code == status.HTTP_403_FORBIDDEN
