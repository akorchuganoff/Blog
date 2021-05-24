from django.urls import path, include
from . import views

urlpatterns = [
    path('article/<int:article_id>', views.article)
]
