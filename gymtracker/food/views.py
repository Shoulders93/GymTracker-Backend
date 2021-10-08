from functools import partial
from django.db.models import manager
from django.http.response import Http404
from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Food
from .serializers import FoodSerializer
from django.contrib.auth.models import User


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_food(request):

    print('User', f"{request.user.id} {request.user.email} {request.user.username}")

    if request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        meals = Food.objects.filter(user_id=request.user.id)
        serializer = FoodSerializer(meals, many=True)
        return Response(serializer.data)

def get_object(pk):
    try:
        return Food.objects.get(pk=pk)
    except Food.DoesNotExist:
        raise Http404

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, pk):
    meals = get_object(pk)
    meals.delete()
    return Response(status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def patch(request, pk):
    meals = get_object(pk)
    serializer = FoodSerializer(meals, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)