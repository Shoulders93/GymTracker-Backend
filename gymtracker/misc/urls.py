from django.urls import path
from rest_framework import views
from misc import views

urlpatterns = [
    path ('', views.user_misc),
    path ('delete/<int:pk>', views.delete),
    path ('patch/<int:pk>', views.patch),
]