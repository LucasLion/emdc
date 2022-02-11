from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from .models import Video, IntroVideo
from .forms import SendMailForm
from django.core.mail import send_mail, BadHeaderError


class ListVideos(ListView):
    model = Video
    context_object_name = "videos"


class IntroVideos(ListView):
    model = Video
    context_object_name = "introvideo"

def index(request):
    title = "EN MATIÈRES DE CONSTRUCTION"
    videos = Video.objects.all()
    intro_video = IntroVideo.objects.all()
    response = render(request, "home/index.html", context={'title': title, 'videos': videos, 'introvideo': intro_video})
    return response

def contact(request):
    title = "EN MATIÈRES DE CONSTRUCTION"

    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            send_email(request, form.cleaned_data)
            return HttpResponse("merci merci")
    else:
        form = SendMailForm()


    response = render(request, "home/contact.html", context={'title': title, "form": form})
    return response

def send_email(request,data):
    subject = request.POST.get('subject', data['object'])
    from_email = request.POST.get('message', data['email'])
    # a faire: rendre l'envoi de mails plus lisible
    #phone = data['phone']
    #adress = data['adress']
    #zip_code = data['zip_code']
    # message = f"{data['message']} \n{phone}\n{adress}\n{zip_code}"
    message = request.POST.get('from_email', data['message'])
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['lucaslion7@gmail.com'],)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return HttpResponse("mail envoyé")
    else:
        return HttpResponse("mauvais champs renseignés")