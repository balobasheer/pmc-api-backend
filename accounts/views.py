from .models import User
from rest_framework import generics

from .serializers import UserSerializer, UserRegisterSerializer, LoginSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


class ActiveUsersListAPIView(APIView):
    permission_class = [IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.filter(is_deleted=False)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeletedUsersListAPIView(APIView):
    permission_class = [IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.filter(is_deleted=True)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            }
        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]
            },
            status=status.HTTP_201_CREATED
        )
        

class UserLoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK,
            )


