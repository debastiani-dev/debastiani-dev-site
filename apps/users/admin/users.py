from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Use email instead of username
    ordering = ["email"]
    list_display = ["email", "fullname", "is_staff", "is_active", "created_at"]
    list_filter = ["is_active", "is_admin"]
    search_fields = ["email", "first_name", "last_name"]

    # Override fieldsets to use our custom fields and remove 'username'/'date_joined'
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "photo", "phone_number")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {"fields": ("last_login", "created_at", "modified_at")},
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password",
                    "confirm_password",
                ),
            },
        ),
    )

    readonly_fields = ["created_at", "modified_at"]
