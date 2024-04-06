from django.contrib.auth.models import User
from rest_framework import serializers

from services.models import Service, NewService


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = (
            'name',
            'photo',
            'description',

        )

    read_only_field = ['is_deleted', 'created', 'updated']