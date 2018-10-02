from django.shortcuts import render

from .models import Meal

# Create your views here.
def index(request):
    meals = Meal.objects.order_by('-date')
    context = {'meals': meals}
    return render(request, 'meals/index.html', context)
