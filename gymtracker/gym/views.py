from django.db.models import manager
from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

# from gymtracker import gym
from .models import Gym
from .serializers import GymSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([AllowAny])

def get_all_exercises(request):
    exercises = Gym.objects.all()
    serializer = GymSerializer(exercises, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_exercises(request):

    print('User', f"{request.user.id} {request.user.email} {request.user.username}")

    if request.method == 'POST':
        serializer = GymSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        exercises = Gym.objects.filter(user_id=request.user.id)
        serializer = GymSerializer(exercises, many=True)
        return Response(serializer.data)





# class GymList(APIView):

#     # permission_classes = [IsAuthenticated]

#     permission_classes = [AllowAny]

#     def get(self, request):
#         gym = Gym.objects.all()
#         serializer = GymSerializer(gym, many=True)
#         return Response(serializer.data)