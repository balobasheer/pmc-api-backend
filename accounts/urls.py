from django.urls import path

from .views import UserListAPIView, UserRegisterAPIView, UserLoginAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='home'),
    # path('<int:pk>/', UserListAPIView.as_view(), name='user_detail'),
    path('create/', UserRegisterAPIView.as_view(), name='create'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    
]