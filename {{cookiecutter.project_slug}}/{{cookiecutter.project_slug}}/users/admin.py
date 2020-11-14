# Django
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

# Third Party Libraries
from sorl.thumbnail.admin import AdminImageMixin

# Local
from .forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(AdminImageMixin, auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        ("User", {"fields": ("name", "avatar")}),
    ) + auth_admin.UserAdmin.fieldsets

    list_display = ["username", "name", "email", "is_superuser"]
    search_fields = ["name", "email", "username"]
