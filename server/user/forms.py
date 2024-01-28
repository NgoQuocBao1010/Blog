from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "fullname")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "username", "fullname")
