from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.managers import CustomUser


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50 , blank=False, verbose_name="Иия и фамилия пользователя")
    email = models.EmailField(unique=True, verbose_name="Почта", blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    objects = CustomUser()

    def __str__(self):
        return self.username


