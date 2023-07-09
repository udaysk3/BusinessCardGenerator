from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous')
    phone  = models.CharField(max_length=20, default='0000000000')
    paid_member = models.BooleanField(default=False)
    