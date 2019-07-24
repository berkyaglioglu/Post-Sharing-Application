from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from .managers import Manager
# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    first_name = models.TextField(max_length=50, blank=False, verbose_name='first name')
    last_name = models.TextField(max_length=50, blank=False, verbose_name='last name')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = Manager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


