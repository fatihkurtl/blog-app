from rest_framework import serializers
from .models import SubscribeVisitors


class SubscribeVisitorsSerializer(serializers.ModelSerializer):
    class Meta:
        models = SubscribeVisitors
        fields = '__all__'