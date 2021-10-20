from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """User Model"""

    bio = models.TextField(default="", blank=True)
