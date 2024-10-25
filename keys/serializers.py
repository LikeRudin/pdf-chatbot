from rest_framework.serializers import ModelSerializer, Serializer, CharField
from rest_framework.exceptions import ValidationError 
from .models import Key


class KeyEnrollSerializer(Serializer):
    kind = CharField(write_only=True)
    api_key = CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, data):
        name = data.get("name")
        kind = data.get("kind")
        api_key = data.get("api_key")
        

        if not(name and kind and api_key):
            raise ValidationError("서비스 제공자와 api key를 모두 선택해야 합니다.")
        return data 

  
class KeySerializer(ModelSerializer):
    class Meta:
        model = Key;
        fields = "__all__" 