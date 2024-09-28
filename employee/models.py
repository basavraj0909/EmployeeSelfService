from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class EmployeeManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class Employee(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)  # Auto-incremented unique user ID
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    position = models.CharField(max_length=20, default='NA')

    # Additional Profile Information
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EmployeeManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    # Alias for the primary key
    @property
    def id(self):
        return self.user_id

    def __str__(self):
        return f"{self.username} - {self.position}"
