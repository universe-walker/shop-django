from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator
)
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """User does not have a username and is identified by a unique email."""
    username = None
    email = models.EmailField(_('Email'), max_length=100, unique=True)
    first_name = models.CharField(_('Имя'), max_length=40, validators=[MaxLengthValidator(40), MinLengthValidator(2)])
    last_name = models.CharField(_('Фамилия'),
                                 max_length=40,
                                 validators=[MaxLengthValidator(40), MinLengthValidator(2)])
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.__str__()
