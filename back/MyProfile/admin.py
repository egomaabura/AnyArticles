from typing import Any
from django.contrib import admin
from django_boost.admin import LogicalDeletionModelAdmin
from .models import User


@admin.register(User)
class UserAdmin(LogicalDeletionModelAdmin):
    list_display = (
        "name",
        "mail",
        "id",
        "deleted_at",
    )
    search_fields = (
        "name",
        "mail",
        "id",
    )
    list_per_page = 30
    ordering = (
        "created_at",
        "updated_at"
    )
    exclude = (
        "id",
        "created_at",
        "updated_at",
    )
