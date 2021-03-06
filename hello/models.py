from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]
