from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from openapi.models import Performance


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

    def create_facebook_user(self, email, facebook_id, password=None):
        user = MyUser(
            email=email,
            facebook_id=facebook_id)
        user.is_facebook = True
        user.is_active = True
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    bookmark_performance = models.ManyToManyField(
        Performance,
        blank=True,
        through='Bookmark',
    )
    facebook_id = models.CharField(max_length=50, blank=True)
    is_facebook = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class Bookmark(models.Model):
    user = models.ForeignKey(MyUser)
    content = models.ForeignKey(Performance)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('user', 'content')
        )
