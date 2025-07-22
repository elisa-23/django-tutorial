from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Users(AbstractUser):

    USER = 1
    SUPERVISOR = 2
    ROLE_CHOICES = ((USER, 'user'), (SUPERVISOR, 'supervisor'))
    role = models.CharField(choices=ROLE_CHOICES, null=False, default=(USER, 'user'))

    username = models.CharField(max_length=255, null=False, unique=True)
    email = models.EmailField(null=False, unique=True)            #parenthesis can't be empty
    #password = models.CharField(max_length=255, null=False)      #might not be needed since it was created in Abstract User

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
    	return "{}".format(self.email)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Ensures the password is hashed
        user.save(using=self._db)
        return user

class Quizzes(models.Model):
    types = models.JSONField()
    title = models.CharField(max_length=255, null=False)
    creator = models.ForeignKey(Users, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Questions(models.Model):
    question = models.CharField(max_length=255, null=False)
    answer = models.JSONField(default=list)
    incorrect = models.JSONField(default=list, blank=True, null=True)
    quiz = models.ForeignKey(Quizzes, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)