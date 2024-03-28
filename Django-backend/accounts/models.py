from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you want
    # For example, to add a date of birth field:
    date_of_birth = models.DateField(null=True, blank=True)
