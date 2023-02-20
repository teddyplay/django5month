from django.contrib.auth.models import BaseUserManager


class CustomUser(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if email is None:
            return ValueError("У вас нет почты!")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        return self.create_user(email=email, password=password, **extra_fields)
