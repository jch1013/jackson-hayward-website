from django.shortcuts import render
from django.http import HttpResponse
from .models import TimelineItem
from .models import Project



# Home page view
def home(request):
    return render(request, 'main/home.html')

# Projects view
def projects(request):
    project_items = Project.objects.all()
    return render(request, 'projects.html', {'project_items' : project_items})

# Experience me view
def experience(request):
    timeline_items = TimelineItem.objects.all()
    return render(request, 'experiences.html', {'timeline_items': timeline_items})

# About me view
def about_me(request):
    return render(request, 'about_me.html')
