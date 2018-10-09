from django.db import models
from django.forms import ModelForm

# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    date = models.DateTimeField()

class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['title', 'description', 'date']
