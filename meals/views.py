from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Meal, MealForm

def index(request):
    meals = Meal.objects.order_by('-date')
    context = {'meals': meals}
    return render(request, 'meals/index.html', context)

def add(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MealForm()

    return render(request, 'meals/add.html', {'form': form})
