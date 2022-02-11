from django.contrib import admin
from .models import Video, IntroVideo
from embed_video.admin import AdminVideoMixin


class UploadVideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ("title", "description", "video")
    list_editable = ("description", "video")


class VideoIntro(AdminVideoMixin, admin.ModelAdmin):
    list_display = ("video", )


admin.site.register(Video, UploadVideoAdmin)
admin.site.register(IntroVideo, VideoIntro)

