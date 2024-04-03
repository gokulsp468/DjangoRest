from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.TextField(max_length=20)
    age = models.IntegerField()
    
