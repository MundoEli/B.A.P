from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sdaqwfewfqw', views.about, name='about'),
    path('create', views.add, name='add')
]
