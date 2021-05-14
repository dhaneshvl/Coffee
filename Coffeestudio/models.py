from django.db import models

# Create your models here.

class Register(models.Model):

    Name = models.CharField(max_length=50)

    Password = models.CharField(max_length=50)

    Age = models.IntegerField()
    Address = models.CharField(max_length=100)
    Phone = models.IntegerField()
