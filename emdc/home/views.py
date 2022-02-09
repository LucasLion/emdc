from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Video

def index(request):
    title = "EN MATIÈRES DE CONSTRUCTION"
    videos = Video.objects.all()
    response = render(request, "home/index.html", context={'title': title, 'videos': videos})
    return response


class ListVideos(ListView):
    model = Video
    context_object_name = "videos"


