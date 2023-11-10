from rest_framework import serializers
from .models import MEMBER, SocialMediaLink

class MEMBERSerializer(serializers.ModelSerializer):    
    class Meta:
        model = MEMBER
        fields = '__all__'
        
class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'