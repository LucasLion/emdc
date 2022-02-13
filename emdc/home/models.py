from pathlib import Path
from django.core.exceptions import ValidationError
from django.db import models
from moviepy.editor import *
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to="video/")

    def __str__(self):
        return self.title

    # actually not working
    def generate_video_thumbnail(self):
        thumbnail_dir = os.path.join(BASE_DIR, '../media_root/thumbnails')
        os.makedirs(thumbnail_dir, exist_ok=True)

        clips = VideoFileClip(self.video)
        frames = clips.reader.fps
        duration = clips.duration

        max_duration = int(duration)+1

        i = max_duration//5

        frame = clips.get_frame(i)

        new_img_file = os.path.join(thumbnail_dir, f"{i}.jpg")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_file)
        print("thumbnail created")


class IntroVideo(models.Model):
    video = models.FileField(upload_to="video/%y")

    def save(self, *args, **kwargs):
        if not self.pk and IntroVideo.objects.exists():
            raise ValidationError("Vous avez déja ajouté votre vidéo d'introduction")
        return super(IntroVideo, self).save(*args, **kwargs)