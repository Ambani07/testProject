from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, user_type, password=None):
        if not email:
            return ValueError("User must have an email address")

        if not username:
            return ValueError("User must have a username")

        if not user_type:
            return ValueError("User must have a type")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            user_type=user_type
        )

        user.set_password(password)
        user.save(user=self._db)
        return user

    def create_superuser(self, email, username, user_type, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            user_type=user_type,
            password=password
        )

        if user_type == "employer":
            user.is_employer = True
        elif user_type == "jobseeker":
            user.is_jobseeker = True
        else:
            user.is_admin = True
            user.is_superuser = True

        user.save(using=self._db)


# Create your models here.
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_employer = models.BooleanField(default=False)
    is_jobseeker = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type']

    def __set__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
