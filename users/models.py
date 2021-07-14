from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):
    first_name = None
    last_name = None
    username = None

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.PositiveBigIntegerField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]
    objects = CustomUserManager()

    def __str__(self):
        return self.name

