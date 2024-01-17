from rest_framework import serializers
from .models import StartupProgress

class StartupSerializers(serializers.ModelSerializer):
    class Meta:
        model = StartupProgress
        fields = '__all__'