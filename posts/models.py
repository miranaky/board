from django.db import models
from django.utils.timezone import now
from users import models as user_models


class Post(models.Model):

    """Post Model Config"""

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    title = models.CharField(max_length=180, blank=False, null=True)
    author = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)
