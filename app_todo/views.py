# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer,tagSerializer
from .models import TodoDetails,tag
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TagViewSet(viewsets.ModelViewSet):
    queryset = tag.objects.all()
    serializer_class = tagSerializer
    permission_classes = [IsAuthenticated]

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = TodoDetails.objects.all()
    permission_classes = [IsAuthenticated]