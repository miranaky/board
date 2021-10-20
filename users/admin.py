from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = (("Profile", {"fields": ("username", "first_name", "last_name", "email", "bio")}),)

    list_display = ("username", "first_name", "last_name")
