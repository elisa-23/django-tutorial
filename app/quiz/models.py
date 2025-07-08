from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(models.Model):
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"

    username = models.CharField(max_length=255, null=False, unique=True)
    email = models.EmailField(null=False, unique=True)            #parenthesis can't be empty
    password = models.CharField(max_length=255, null=False)
    
    type = models.CharField(
        max_length=20, choices=Types.choices, default=Types.USER
    )
    def __str__(self):
    	return self.username

class Quizzes(models.Model):
    title = models.CharField(max_length=255, null=False)
    category = models.