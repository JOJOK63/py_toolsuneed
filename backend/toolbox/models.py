from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

#
# class UserProfile(AbstractUser):
#     """Database model for users in the system"""
#     email = models.EmailField(max_length=255, unique=True)
#     image = models.ImageField(upload_to="images/", null=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     def get_full_name(self) -> str:
#         """Retrieve full name of user"""
#         return f"{self.first_name} {self.last_name}".strip()
#
#     def __str__(self) -> str:
#         """Return string representation of user"""
#         return self.email
