from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer, CustomTokenObtainPairSerializer


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == "manager":
            users = User.objects.filter(role='staff')
            serializer = UserSerializer(users, many=True)
            response = {"user_data":{"username":request.user.username, "email":request.user.email}, "staff_data":serializer.data}
        else:
            response = {"user_data":{"username":request.user.username, "email":request.user.email}, "staff_data":[]}
        return Response(response)
    
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
