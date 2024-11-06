from rest_framework.serializers import ModelSerializer

from .models import Conversation,Message

class ConversationListSerializer(ModelSerializer):
    class Meta:
        model = Conversation
        fields = ("title", "id")

class MessageSerializer(ModelSerializer):
    class Meta: 
        model = Message
        fields = "__all__"


class ConversationWithMessageSerializer(ModelSerializer):
    message = MessageSerializer(many=True, read_only=True)

    class Meta: 
        model = Conversation
        fields = ("title", "id", "messages")
