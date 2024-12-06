from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Shift, WeeklyOff
from .serializers import ShiftSerializer, WeeklyOffSerializer

class ShiftViewSet(ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [IsAuthenticated]

class WeeklyOffViewSet(ModelViewSet):
    queryset = WeeklyOff.objects.all()
    serializer_class = WeeklyOffSerializer
    permission_classes = [IsAuthenticated]
