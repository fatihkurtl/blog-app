from rest_framework import serializers
from .models import POST, COMMENT

# class MEMBERSerializer(serializers.ModelSerializer):    
#     class Meta:
#         model = MEMBER
#         fields = '__all__'
        
class POSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = POST
        fields = '__all__'
    language = serializers.ChoiceField(choices=POST.LANGUAGES, default='tr')
    
class COMMENTSerializer(serializers.ModelSerializer):
    class Meta:
        model = COMMENT
        fields = '__all__'

# class CONTACTSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CONTACT
#         fields = '__all__'