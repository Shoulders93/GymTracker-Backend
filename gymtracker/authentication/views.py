from django.contrib.auth.model import User
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework import AllowAny
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
