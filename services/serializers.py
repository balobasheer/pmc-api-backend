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
            'is_deleted',
            'created', 
            'updated',

        )


class NextedServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = (
            'name',
        )
        read_only_field = ('created', 'updated')

class NewServiceRequestSerializer(serializers.ModelSerializer):
    service_type = NextedServiceSerializer(many=True, read_only=True)
    class Meta:
        model = NewService
        fields = (
            'service_type',
            'name',
            'customer_phone_number',
            'customer_email',
            'post_code',
            'job_nature',
            'status',
            'address',
            'service_picture',
        )
    read_only_field = ('created', 'updated')

    def create(self, validated_data):
        print(validated_data)
        services = validated_data.pop('service_type')
        new_service = NewService.objects.create(**validated_data)
        for service in services:
            Service.objects.create(newservice=new_service, **services)
        return new_service