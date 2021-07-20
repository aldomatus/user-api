# rest framework
from rest_framework import generics, filters

# Django filters
from django_filters.rest_framework import DjangoFilterBackend  

from .models.users import User 
from .serializers import UserSerializer

class ListUser(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer