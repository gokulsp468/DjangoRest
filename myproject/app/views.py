from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from . import models
from . import serializers
# Create your views here.
class MessageCreateView(generics.CreateAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']
    

class MessageListView(generics.ListAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    http_method_names = ['get']
    