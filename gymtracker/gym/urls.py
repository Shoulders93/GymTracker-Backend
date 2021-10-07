from django.urls import path
from rest_framework import views
from gym import views

urlpatterns = [
    path ('', views.GymList.as_view())
]