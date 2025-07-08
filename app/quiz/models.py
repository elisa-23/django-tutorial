from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

class Role(models.Model):
    USER = 1
    ADMIN = 2
    ROLE_CHOICES = ((USER, 'user'), (ADMIN, 'admin'))

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()

# Create your models here.
class Users(AbstractUser):
    role = models.ForeignKey(Role, null=False)

    username = models.CharField(max_length=255, null=False, unique=True)
    email = models.EmailField(null=False, unique=True)            #parenthesis can't be empty
    #password = models.CharField(max_length=255, null=False)      #might not be needed since it was created in Abstract User

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
    	return "{}".format(self.email)

class Type(models.Model):
    MULTIPLE_CHOICE = 1
    BOOLEAN = 2
    DROPDOWN = 3
    NUMERICAL = 4

    TYPE_CHOICES = ((MULTIPLE_CHOICE, 'multiple choice'), (BOOLEAN, 'boolean'), (DROPDOWN, 'dropdown'), (NUMERICAL, 'numerical'))

    id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()

class Quizzes(models.Model):
    title = models.CharField(max_length=255, null=False)
    types = models.ManyToManyField(Type, null=False)
    creator = models.ForeignKey(Users, null=False)

    def __str__(self):
        return self.title

class Questions(models.Model):
    question = models.CharField(max_length=255, null=False)
    answer = ArrayField(models.CharField(max_length=200), blank=False, default=list, null=False)
    incorrect = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    quiz = models.ForeignKey(Quizzes, null=False)

