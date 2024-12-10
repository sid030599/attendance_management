from rest_framework.permissions import IsAuthenticated
from .models import WeeklyOff
from rest_framework.response import Response
from .serializers import WeeklyOffSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import WeeklyOff, UserShiftMapping
from .serializers import UserShiftSerializer, WeeklyOffSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = UserShiftMapping.objects.all()
    serializer_class = UserShiftSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.role == "manager":
            return Response(self.serializer_class(self.queryset, many=True).data)
        else:
            queryset = self.queryset.filter(staff=user)
            return Response(self.serializer_class(queryset, many=True).data)


class WeeklyOffViewSet(viewsets.ModelViewSet):
    queryset = WeeklyOff.objects.all()
    serializer_class = WeeklyOffSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.role == "manager":
            return Response(self.serializer_class(self.queryset, many=True).data)
        else:
            queryset = self.queryset.filter(staff=user)
            return Response(self.serializer_class(queryset, many=True).data)
