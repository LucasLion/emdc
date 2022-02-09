from django.db import models
from django.db import models
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to="video/%y")

    def __str__(self):
        return self.title
