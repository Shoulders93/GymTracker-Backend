from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import logout
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

def logout_request(request):
    logout(request)
