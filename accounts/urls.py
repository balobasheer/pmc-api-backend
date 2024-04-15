from django.urls import path

from .views import (ActiveUsersListAPIView,
                    DeletedUsersListAPIView, 
                    UserRegisterAPIView,
                    UserLoginAPIView
                    )

urlpatterns = [
    path('', ActiveUsersListAPIView.as_view(), name='home'),
    path('deleted', DeletedUsersListAPIView.as_view(), name='user_detail'),
    path('create/', UserRegisterAPIView.as_view(), name='create'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    
]