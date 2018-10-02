from django.db import models

# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    date = models.DateTimeField()
