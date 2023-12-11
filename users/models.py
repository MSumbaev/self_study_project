from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Класс Юзер"""
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
