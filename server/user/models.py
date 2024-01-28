from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, username, fullname, password):
        if not email:
            raise ValueError(_("The Email field must be set"))
        if not username:
            raise ValueError(_("The Username field must be set"))
        if not fullname:
            raise ValueError(_("The Fullname field must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, fullname=fullname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, fullname, password):
        user = self.create_user(email, username, fullname, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    fullname = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "fullname"]

    objects = UserManager()

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(User, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email
