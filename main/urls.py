from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('projects/', views.projects, name='projects'), 
    path('about/', views.about_me, name='about_me'),
    path('experience/', views.experience, name='experiences')
]