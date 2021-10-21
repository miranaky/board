import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from model_bakery import baker

from users.models import User
from posts.models import Post


class TestPostModels(TestCase):
    """Test Post model"""

    def setUp(self) -> None:
        if isinstance(Post, type):
            self.model = baker.make(Post)

    def test_create_post_models(self):
        assert self.model


# --------------------------------------


class TestPostViews(APITestCase):
    """Teset Post views"""

    def setUp(self) -> None:
        self.client = APIClient()
        # 더미 유저 생성
        self.password = "password"
        self.user = User.objects.create(
            username="kaengkaeng",
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

    def create_new_post(self, number=0):
        url = "/api/v1/posts/"
        post_data = json.dumps({"title": f"New Post{number}", "content": f"New Post contents{number}"})
        res = self.client.post(url, post_data, content_type="application/json", HTTP_AUTHORIZATION=self.http_author)
        return res

    def test_get_posts(self):

        """Get list of posts"""

        url = "/api/v1/posts/"
        res = self.client.get(url, {}, content_type="application/json")
        assert res.status_code == status.HTTP_200_OK
        assert res.data.get("count") == 0

    def test_create_new_post(self):

        """Create a new post by authenticated user"""

        # url = "/api/v1/posts/"
        # post_data = json.dumps({"title": "New Post", "content": "New Post contents"})
        # res = self.client.post(url, post_data, content_type="application/json", HTTP_AUTHORIZATION=self.http_author)
        res = self.create_new_post()
        assert res.status_code == status.HTTP_201_CREATED
        assert res.data.get("author").get("username") == self.user.username

        url = "/api/v1/posts/"
        post_data = json.dumps({"title": "New Post", "content": "New Post contents"})
        unauth_res = self.client.post(url, post_data, content_type="application/json")
        assert unauth_res.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_existent_post(self):

        """Get a existent post"""

        post_id = self.create_new_post().data.get("id")
        existent_url = f"/api/v1/posts/{post_id}"
        res = self.client.get(existent_url, {}, content_type="application/json")
        assert res.status_code == status.HTTP_200_OK

    def test_get_non_existent_post(self):

        """Get a non existent post"""

        non_existent_url = "/api/v1/posts/9999"
        res = self.client.get(non_existent_url, {}, content_type="application/json")
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_update_post_by_created_user(self):

        """Update a post by created user"""

        post_id = self.create_new_post().data.get("id")
        url = f"/api/v1/posts/{post_id}"
        update_post_data = json.dumps({"title": "Update title", "content": "Update content"})
        res = self.client.put(
            url, update_post_data, content_type="application/json", HTTP_AUTHORIZATION=self.http_author
        )
        assert res.status_code == status.HTTP_200_OK
        assert res.data.get("author").get("username") == self.user.username

    def test_update_post_by_different_user(self):

        """Update a post by different user"""

        post_id = self.create_new_post().data.get("id")
        url = f"/api/v1/posts/{post_id}"
        update_post_data = json.dumps({"title": "Update title", "content": "Update content"})
        http_author = "X-JWT DIFFERENT USER TOKEN"
        res = self.client.put(url, update_post_data, content_type="application/json", HTTP_AUTHORIZATION=http_author)
        assert res.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_post_by_created_user(self):

        """Delete a post by created user"""

        post_id = self.create_new_post().data.get("id")
        url = f"/api/v1/posts/{post_id}"
        res = self.client.delete(url, {}, content_type="application/json", HTTP_AUTHORIZATION=self.http_author)
        assert res.status_code == status.HTTP_200_OK

    def test_delete_post_by_different_user(self):

        """Delete a post by different user"""

        post_id = self.create_new_post().data.get("id")
        url = f"/api/v1/posts/{post_id}"
        http_author = "X-JWT DIFFERENT USER TOKEN"
        res = self.client.delete(url, {}, content_type="application/json", HTTP_AUTHORIZATION=http_author)
        assert res.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_non_existent_post(self):

        """Delete a non existent post by created user"""

        url = "/api/v1/posts/99999"
        res = self.client.delete(url, {}, content_type="application/json", HTTP_AUTHORIZATION=self.http_author)
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_get_50_posts(self):

        """Create 50 posts and Get list of posts"""

        for i in range(50):
            self.create_new_post(i)

        url = "/api/v1/posts/"
        res = self.client.get(url, {}, content_type="application/json")
        limit = 30
        assert res.status_code == status.HTTP_200_OK
        assert res.data.get("count") == 50
        assert len(res.data.get("results")) == limit

    def test_get_50_posts_with_limit_10(self):

        """Create 50 posts and Get list of  10  posts"""

        for i in range(50):
            self.create_new_post(i)

        url = "/api/v1/posts/?limit=10"
        res = self.client.get(url, {}, content_type="application/json")
        limit = 10
        assert res.status_code == status.HTTP_200_OK
        assert res.data.get("count") == 50
        assert len(res.data.get("results")) == limit
        assert res.data.get("results")[-1].get("id") == 10
