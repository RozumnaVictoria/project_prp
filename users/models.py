from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from users.manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', unique=True)
    number_tel = models.CharField(max_length=12, verbose_name='Мобільний номер')
    first_name = models.CharField(max_length=50, blank=True, verbose_name='Імя')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Прізвище')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
