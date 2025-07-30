from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.set_password(password)  # Ensures the password is hashed
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', CustomUser.SUPERVISOR)
        return self.create_user(email, password, **extra_fields)

# Create your models here.
class CustomUser(AbstractUser):
    role = models.IntegerField(null=False, default=1)
    username = models.CharField(max_length=255, null=False, unique=True)
    email = models.EmailField(null=False, unique=True)            #parenthesis can't be empty
    #password = models.CharField(max_length=255, null=False)      #might not be needed since it was created in Abstract User

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role']

    objects = CustomUserManager()

    def __str__(self):
    	return "{}".format(self.email)

class Quiz(models.Model):
    title = models.CharField(max_length=255, null=False)
    creator = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Question(models.Model):
    question = models.CharField(max_length=255, null=False)
    answers = models.ManyToManyField('Answer', null=False, blank=True, related_name='answers')
    quiz = models.ForeignKey(Quiz, null=False, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=255, null=False, default='multiple choice')

    def __str__(self):
        return str(self.id)
    
class Answer(models.Model):
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, null=False)
    correct = models.BooleanField(null=False)

    def __str__(self):
        return str(self.id)