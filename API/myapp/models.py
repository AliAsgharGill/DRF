from django.db import models

# Create your models here.
class StudentData(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)