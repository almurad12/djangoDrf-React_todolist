from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializers
from rest_framework import viewsets
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()
