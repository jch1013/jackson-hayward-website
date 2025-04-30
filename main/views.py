from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'main/home.html')

def timeline(request):
    return render(request, 'timeline.html')

def projects(request):
    return render(request, 'projects.html')


def about_me(request):
    return render(request, 'about_me.html')

def experience(request):
    return render(request, 'experiences.html')

def projects(request):
    return render(request, 'projects.html')