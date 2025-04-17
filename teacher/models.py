# teacher/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    # Add any additional fields for teachers here
    phone_number = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.username