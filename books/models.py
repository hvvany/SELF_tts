from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    x = models.IntegerField()
    y = models.IntegerField()
