from rest_framework import serializers
from .models import POST, COMMENT, POST_LIKE, POST_SAVE
        
class POSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = POST
        fields = '__all__'
    # language = serializers.ChoiceField(choices=POST.LANGUAGES, default='tr')
    
class COMMENTSerializer(serializers.ModelSerializer):
    class Meta:
        model = COMMENT
        fields = '__all__'

class POST_LIKESerializer(serializers.ModelSerializer):
    class Meta:
        model = POST_LIKE
        fields = '__all__'

class POST_SAVESerializer(serializers.ModelSerializer):
    class Meta:
        model = POST_SAVE
        fields = '__all__'