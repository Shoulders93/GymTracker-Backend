from rest_framework import serializers
from .models import Gym

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ['id', 'date', 'exercise', 'sets', 'reps', 'weight', 'user_id']