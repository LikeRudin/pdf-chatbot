from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied

from .serializers import ConversationListSerializer, MessageSerializer
from .models import Conversation, Message

from libs.response import ResponseDict
from libs.ExceptionAPIView import ExceptionAPIView

class Conversations(ExceptionAPIView):
    def get(self, request):
        all_conversations = Conversation.objects.filter(user_id=request.user.id).filter(is_deleted=False)
        serializer = ConversationListSerializer(all_conversations, many=True)
        
        return Response(ResponseDict(success=True, message="read conversation list of user", data=serializer.data, errors=None), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ConversationListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user.id)
            return Response(ResponseDict(success=True, message="create a conversation", data=serializer.data, errors=None),status=status.HTTP_201_CREATED)
        return Response(ResponseDict(success=False, message="failed to create a conversation",data=None, errors=serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class AConversation(ExceptionAPIView):

    def get(self, request, pk):
        return
    
    def delete(self, request, pk):
        conversation = Conversation.objects.get(pk=pk)
        conversation.delete()
        return Response(ResponseDict(success=True, message="Conversation deleted successfully"), status=status.HTTP_200_OK)
    

class ConversationWithMessages(ExceptionAPIView):
    permission_classes = [IsAuthenticated]

    def get_conversation(self, request, pk):
        try:
            conversation = Conversation.objects.get(pk=pk)
        except Conversation.DoesNotExist:
            raise NotFound("No conversation found.")
        if conversation.user != request.user:
            raise PermissionDenied("Only the owner can access this conversation.")
        return conversation 
    
    def get(self, request, pk):
            conversation = self.get_conversation(request,pk)
            messages = Message.objects.filter(conversation=conversation)
            serializer = MessageSerializer(messages, many=True)
            return Response(ResponseDict(success=True, message=f"messages from conversation{conversation.title}", data=serializer.data),
                status=status.HTTP_200_OK
            )

    
    def post(self,request,pk):
            conversation = self.get_conversation(request,pk)
            serializer = MessageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=request.user.id, conversation_id=conversation.id)
                return Response(ResponseDict(success=True, message="Message created successfully",data=serializer.data),status=status.HTTP_201_CREATED)
        
            return Response(ResponseDict(success=False, message="Validation error. Not Valid Message", data=None, errors= serializer.erros),
                            status=status.HTTP_400_BAD_REQUEST)
