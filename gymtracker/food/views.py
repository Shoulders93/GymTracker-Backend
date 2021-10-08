from functools import partial
from django.db.models import manager
from django.http.response import Http404
from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Gym
from .serializers import GymSerializer
from django.contrib.auth.models import User


