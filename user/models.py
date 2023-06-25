from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    paid_member = models.BooleanField(default=False)
    