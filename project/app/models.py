from django.db import models

# Create your models here.

class User(models.Model):
    name = models.TextField()
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    
    