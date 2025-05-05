from django.contrib import admin
from .models import TimelineItem
from .models import Project

# Register your models here.
admin.site.register(TimelineItem)
admin.site.register(Project)
