from django.shortcuts import render
from rest_framework import viewsets
from .models import Story, Author
from .serializers import StorySerializer, AuthorSerializer

class StoryView(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
