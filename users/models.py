from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_delivery_agent = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']
