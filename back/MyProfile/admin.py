from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "mail",
        "user_id",
        "deleted_at",
    )
    search_fields = (
        "name",
        "mail",
        "user_id",
    )
    list_per_page = 30
    ordering = (
        "created_at",
        "updated_at"
    )
    exclude = (
        "user_id",
        "created_at",
        "updated_at",
    )

admin.site.register(User, UserAdmin)