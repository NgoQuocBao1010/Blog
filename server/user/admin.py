from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.forms import UserCreationForm, UserChangeForm
from user.models import User


# Create a custom admin class for the User model
class AppUserAdmin(UserAdmin):
    add_form = UserCreationForm  # Use the custom User creation form for adding users
    form = UserChangeForm  # Use the custom User change form for editing users
    model = User  # Set the model to use for the admin interface

    # Define the columns to display in the user list view in the admin panel
    list_display = (
        "email",
        "username",
        "fullname",
        "is_staff",
        "is_active",
    )

    # Add filters to the user list view for convenient searching
    list_filter = (
        "email",
        "username",
        "fullname",
        "is_staff",
        "is_active",
    )

    # Define the sections and fields for user editing in the admin panel
    fieldsets = (
        (None, {"fields": ("email", "password")}),  # Basic user information
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),  # Permissions and groups
    )

    # Define the fields for adding a new user in the admin panel
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )

    # Define fields to search for users in the admin panel
    search_fields = ("email", "username", "fullname")

    # Define the default ordering for users in the admin panel
    ordering = ("email",)


admin.site.register(User, AppUserAdmin)
