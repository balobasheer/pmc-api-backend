from django.urls import path

from .views import ServiceAPIView, NewServiceRequestAPIView, AllServicesAPIView

urlpatterns = [
    path('', AllServicesAPIView.as_view(), name='create_service'),
    path('create/', ServiceAPIView.as_view(), name='services'),
    path('new-service-request/', NewServiceRequestAPIView.as_view(), name='new_service_request'),
    
]