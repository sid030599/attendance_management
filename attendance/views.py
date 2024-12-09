from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsManager
from .models import AttendanceRecord
from roster.models import Shift
from attendance.serializers import AttendanceRecordSerializer
from datetime import datetime, timedelta

class AttendanceRecordViewSet(ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    
    def get_permissions(self):
        """
        Override this method to provide different permissions for different actions.
        """
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsManager]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        staff = self.request.user
        shift = serializer.validated_data['shift']
        now = datetime.now()
        shift_start = datetime.combine(now.date(), shift.start_time)
        shift_end = datetime.combine(now.date(), shift.end_time)

        # Check if within 1 hour of shift start
        is_valid_time = (shift_start - timedelta(hours=1)) <= now <= shift_end
        serializer.save(staff=staff, marked_within_shift_time=is_valid_time)
