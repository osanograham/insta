from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name=models.CharField("First Name",max_length=150,default="")
    last_name=models.CharField("Last Name", max_length=150,default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

        #https://testdriven.io/blog/django-custom-user-model/#abstractuser-vs-abstractbaseuser
        #https://testdriven.io/blog/django-custom-user-model/#abstractuser-vs-abstractbaseuser