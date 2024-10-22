from rest_framework.serializers import ModelSerializer

from .models import Conversation,Message

class ConversationSerializer(ModelSerializer):
    class Meta:
        model = Conversation
        fields = ("title", "id")


class MessageSerializer(ModelSerializer):
    class Meta: 
        model = Message
        fields = "__all__"