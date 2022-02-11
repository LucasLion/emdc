from django.core.exceptions import ValidationError
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

class IntroVideo(models.Model):
    video = models.FileField(upload_to="video/%y")

    def save(self, *args, **kwargs):
        if not self.pk and IntroVideo.objects.exists():
            raise ValidationError("Vous avez déja ajouté votre vidéo d'introduction")
        return super(IntroVideo, self).save(*args, **kwargs)