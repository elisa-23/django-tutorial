from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class Users(AbstractUser):
    USER = 1
    ADMIN = 2
    ROLE_CHOICES = ((USER, 'user'), (ADMIN, 'admin'))
    role = models.CharField(choices=ROLE_CHOICES, null=False, default=(USER, 'user'))

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
    uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=False)
    types = models.ManyToManyField(Type)
    creator = models.ForeignKey(Users, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uuid_id)

class Questions(models.Model):
    uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=255, null=False)
    answer = models.JSONField(default=list)
    incorrect = models.JSONField(default=list, blank=True, null=True)
    quiz = models.ForeignKey(Quizzes, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uuid_id)