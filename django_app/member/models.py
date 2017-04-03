from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from openapi.models.content import Content


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        user = MyUser(
            email=email,
            **extra_fields)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False

        user.save()

        return user

    def _create_user(self, email, password, **extra_fields):
        user = MyUser(
            email=email,
            **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    bookmark_content = models.ManyToManyField(
        Content,
        blank=True,
        through='BookmarkContent',
    )

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class BookmarkContent(models.Model):
    user = models.ForeignKey(MyUser)
    content = models.ForeignKey(Content)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('user', 'content')
        )
