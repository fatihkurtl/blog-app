from rest_framework import serializers
from .models import CONTACT

class CONTACTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CONTACT
        fields = '__all__'