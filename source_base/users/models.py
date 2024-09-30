from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from source_base.core.custom.model import BaseModel
from source_base.users.managers import UserManager


class User(AbstractBaseUser, BaseModel):
    email = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
