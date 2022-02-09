from django.contrib import admin
from .models import Video
from embed_video.admin import AdminVideoMixin


class UploadVideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ("title", "description", "video")
    list_editable = ("description", "video")


admin.site.register(Video, UploadVideoAdmin)
