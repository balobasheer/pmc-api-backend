from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from services.models import Service
from services.serializers import ServiceSerializer, NewServiceRequestSerializer


class ServiceAPIView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    permission_class = [IsAuthenticated]


class AllServicesAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Service.objects.filter(is_deleted=False)


class NewServiceRequestAPIView(generics.CreateAPIView):
    serializer_class = NewServiceRequestSerializer
    permission_class = [IsAuthenticated]