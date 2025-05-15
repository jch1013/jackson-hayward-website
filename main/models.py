from django.db import models

# Create your models here.

# Create a model for timeline items
class TimelineItem(models.Model):
    #  Accept only 4 digits to fit within alloted space
    year = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='timeline_images/')

    def __str__(self):
        return f"{self.year} - {self.title}"
    

# Create a project card model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    github_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
# Hobbies model for about me page
class Hobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hobby_images/')

    def __str__(self):
        return self.name
