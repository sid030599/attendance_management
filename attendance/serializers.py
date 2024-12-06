from rest_framework import serializers
from .models import AttendanceRecord

class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = ['id', 'staff', 'shift', 'timestamp', 'image', 'marked_within_shift_time']
        read_only_fields = ['staff', 'timestamp', 'marked_within_shift_time']  # These are set automatically