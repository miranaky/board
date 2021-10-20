from django.contrib import admin
from . import models


@admin.register(models.Post)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Config"""

    pass
