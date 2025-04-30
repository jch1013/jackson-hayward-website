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