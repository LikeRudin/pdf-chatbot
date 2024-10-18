from rest_framework.serializers import ModelSerializer, Serializer, CharField
from rest_framework.exceptions import ValidationError

from .models import User

class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "first_name",
            "last_name",
            )

class LoginSerializer(Serializer):
    username = CharField(write_only=True)
    password = CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        
        if not username or not password:
            raise ValidationError("username과 password를 모두 입력해야 합니다.")
        return data        


class JoinSerializer(Serializer):
    username = CharField(write_only=True)
    password = CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        
        if not username or not password:
            raise ValidationError("username과 password를 모두 입력해야 합니다.")
        
        if User.objects.filter(username=username).exists():
            raise ValidationError("이미 존재하는 username입니다.")
        
        return data


