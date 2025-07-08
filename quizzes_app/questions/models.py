from django.db import models

# Create your models here.

from django.db import models

class Users(models.Model):
  firstname = models.CharField(max_length=255)      #text fields with a max of 255 characters
  lastname = models.CharField(max_length=255)