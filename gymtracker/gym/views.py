from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Gym
from .serializers import GymSerializer
from django.contrib.auth.models import User


class GymList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        gym = Gym.objects.all()
        serializer = GymSerializer(gym, many=True)
        return Response(serializer.data)