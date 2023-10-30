from rest_framework import serializers
from .models import MEMBER

class MEMBERSerializer(serializers.ModelSerializer):    
    class Meta:
        model = MEMBER
        fields = '__all__'