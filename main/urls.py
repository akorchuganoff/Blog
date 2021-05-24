from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('mylife', views.life),
    path('joboffer', views.offer)
]
