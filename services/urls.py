from django.urls import path

from .views import ServiceAPIView

urlpatterns = [
    path('create/', ServiceAPIView.as_view(), name='service'),
    
]