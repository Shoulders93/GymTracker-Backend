from django.urls import path
from rest_framework import views
from gym import views
# from gymtracker.gym.views import get_object
# from gymtracker.gym.views import user_exercises

urlpatterns = [
    path ('all/', views.get_all_exercises),
    path ('', views.user_exercises),
    path ('delete/<int:pk>', views.delete),
    path ('patch/<int:pk>', views.patch),
]

# urlpatterns = [
#     path ('', views.GymList.as_view())
# ]