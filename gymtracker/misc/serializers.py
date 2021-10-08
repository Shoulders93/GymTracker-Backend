from rest_framework import serializers
from .models import Misc

class MiscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Misc
        fields = ['id', 'date', 'hours_slept', 'bodyweight', 'additional_notes', 'user_id']