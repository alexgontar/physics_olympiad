from django.shortcuts import render
from materials.models import Grade

def home(request):
    grades = Grade.objects.all().order_by('number')
    return render(request, 'core/home.html', {'grades': grades})