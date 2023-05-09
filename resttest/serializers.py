from rest_framework import serializers
from resttest.models import F1Driver

class F1DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = F1Driver
        fields = '__all__'

