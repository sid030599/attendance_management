from rest_framework import serializers
from .models import AttendanceRecord
from users.serializers import UserSerializer
from roster.serializers import ShiftSerializer

class AttendanceRecordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AttendanceRecord
        fields = ['id', 'staff', 'shift', 'timestamp', 'image', 'marked_within_shift_time']
        read_only_fields = ['staff','timestamp', 'marked_within_shift_time']  # These are set automatically

    def to_representation(self, instance):
        # Use nested serializers for representation
        representation = super().to_representation(instance)
        representation['staff'] = UserSerializer(instance.staff).data
        representation['shift'] = ShiftSerializer(instance.shift).data
        return representation