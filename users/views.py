from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from .models import User
from django.contrib.auth import logout
from .serializers import UserSerializer, CustomTokenObtainPairSerializer


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_data = {
            "username": request.user.username,
            "email": request.user.email,
            "role": request.user.role,
        }
        if request.user.role == "manager":
            users = User.objects.filter(role="staff")
            serializer = UserSerializer(users, many=True)
            response = {
                "user_data": user_data,
                "staff_data": serializer.data,
            }
        else:
            response = {
                "user_data": user_data,
                "staff_data": [],
            }
        return Response(response)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)