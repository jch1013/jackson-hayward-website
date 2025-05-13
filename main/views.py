from django.shortcuts import render
from django.http import HttpResponse
from .models import TimelineItem
from .models import Project
from .models import Hobby


# Home page view
def home(request):
    return render(request, 'main/home.html')

# Projects view
def projects(request):
    project_items = Project.objects.all()
    return render(request, 'projects.html', {'project_items' : project_items})

# Experience view
def experience(request):
    timeline_items = TimelineItem.objects.all()
    return render(request, 'experiences.html', {'timeline_items': timeline_items})

# About me view
def about_me(request):
    hobbies_items = Hobby.objects.all()
    return render(request, 'about_me.html', {'hobbies_items': hobbies_items})