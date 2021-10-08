from django.urls import path
from rest_framework import views
from food import views

urlpatterns = [
    path ('all/', views.get_all_exercises),
]