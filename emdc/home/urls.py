
from django.urls import path

from home import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('contact/', views.contact, name='contact'),

]
