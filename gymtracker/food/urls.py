from django.urls import path
from rest_framework import views
from food import views

urlpatterns = [
    path ('', views.user_food),
    path ('delete/<int:pk>', views.delete),
    path ('patch/<int:pk>', views.patch),
]