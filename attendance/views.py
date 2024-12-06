from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import AttendanceRecord
from attendance.serializers import AttendanceRecordSerializer
from datetime import datetime, timedelta

class AttendanceRecordViewSet(ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        staff = self.request.user
        shift = serializer.validated_data['shift']
        now = datetime.now()
        shift_start = datetime.combine(now.date(), shift.start_time)
        shift_end = datetime.combine(now.date(), shift.end_time)

        # Check if within 1 hour of shift start
        is_valid_time = (shift_start - timedelta(hours=1)) <= now <= shift_end
        serializer.save(staff=staff, marked_within_shift_time=is_valid_time)
