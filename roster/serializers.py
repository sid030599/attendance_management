from rest_framework import serializers
from .models import Shift, WeeklyOff

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['id', 'staff', 'day_of_week', 'start_time', 'end_time']

class WeeklyOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyOff
        fields = ['id', 'staff', 'day_of_week']
