from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomerRole(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    USER = 'USER', 'User'


class User(AbstractUser):
    pseudo = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=CustomerRole.choices, default=CustomerRole.USER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
