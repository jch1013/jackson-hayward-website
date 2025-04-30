from django.shortcuts import render
from django.http import HttpResponse
from .models import TimelineItem



# Home page view
def home(request):
    return render(request, 'main/home.html')

# Projects view
def projects(request):
    return render(request, 'projects.html')

# About me view
def about_me(request):
    timeline_items = TimelineItem.objects.all()
    return render(request, 'about_me.html', {'timeline_items': timeline_items})

# Experience view
def experience(request):
    return render(request, 'experiences.html')
