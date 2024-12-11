from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import AttendanceRecord
from rest_framework.response import Response
from attendance.serializers import AttendanceRecordSerializer
from datetime import datetime, timedelta
import pytz

class AttendanceRecordViewSet(ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        staff = self.request.user
        shift = serializer.validated_data['shift']
        india_timezone = pytz.timezone("Asia/Kolkata")

        now = datetime.now(india_timezone)
        shift_start = datetime.combine(now.date(), shift.start_time, tzinfo=india_timezone)
        shift_end = datetime.combine(now.date(), shift.end_time, tzinfo=india_timezone)

        is_valid_time = (shift_start - timedelta(hours=1)) <= now <= shift_end
        serializer.save(staff=staff, marked_within_shift_time=is_valid_time)
        
    def list(self, request):
        user_id = request.user.id
        if request.user.role == "manager":
            records = self.queryset
            data = AttendanceRecordSerializer(records, many=True).data
            return Response(data)
        else:
            records = AttendanceRecord.objects.filter(staff__id=user_id)
            data = AttendanceRecordSerializer(records, many=True).data
            return Response(data)
        
