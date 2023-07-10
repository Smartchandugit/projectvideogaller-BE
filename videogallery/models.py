from django.db import models


# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    videoUrl = models.URLField()
    thumbnail = models.URLField()

    objects = models.Manager()

    def __str__(self):
        return self.title
