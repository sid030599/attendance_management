from rest_framework import serializers
from .models import Shift, WeeklyOff
from users.serializers import UserSerializer

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['id', 'staff', 'day_of_week', 'start_time', 'end_time']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['staff'] = UserSerializer(instance.staff).data
        return representation

class WeeklyOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyOff
        fields = ['id', 'staff', 'day_of_week']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['staff'] = UserSerializer(instance.staff).data
        return representation