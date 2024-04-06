from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics

from services.models import Service
from services.serializers import ServiceSerializer


class ServiceAPIView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    quaryset = Service.objects.all()