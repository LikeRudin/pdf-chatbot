from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied

from .serializers import ConversationSerializer, MessageSerializer
from .models import Conversation, Message

class Conversations(APIView):
    def get(self, request):
        all_conversations = Conversation.objects.filter(user_id=request.user.id).filter(is_deleted=False)
        serializer = ConversationSerializer(all_conversations, many=True)
        
        return Response({"success": True,
            "message": "get Every Conversation of user",
            "data": serializer.data
            }, status=status.HTTP_200_OK)
        

    def post(self, request):
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AConversation(APIView):

    def get(self, request, pk):
        return
    
    def delete(self, request, pk):
        try:
            conversation = Conversation.objects.get(pk=pk)
            conversation.delete()
            return Response({"success": True, "message": "Conversation deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Conversation.DoesNotExist:
            return Response({"success": False, "error": "Conversation not found"}, status=status.HTTP_404_NOT_FOUND)

class ConversationWithMessages(APIView):
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
        try:
            conversation = self.get_conversation(request,pk)
            messages = Message.objects.filter(conversation=conversation)
            serializer = MessageSerializer(messages, many=True)

            return Response({"success": True,
                "message": "messages of chatroom",
                "data": serializer.data,}, 
                status=status.HTTP_200_OK
            )
        
        except NotFound as e:
            return Response({"success": False, "message":e.detail, "errors": e}, status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied as e:
            return Response({"success": False, "message":e.detail, "errors": e}, status=status.HTTP_403_FORBIDDEN)

    
    def post(self,request,pk):
        try:
            conversation = self.get_conversation(request,pk)
            serializer = MessageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=request.user.id, conversation_id=conversation.id)
                return Response({"success": True,
                                 "message": "Message created successfully",
                                 "data": serializer.data},status=status.HTTP_201_CREATED)
        
            return Response({"success": False,
                             "message": "Validation error. Not Valid Message",
                             "errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        
        except NotFound as e:
            return Response({"success": False, "message":e.detail, "errors": e}, status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied as e:
            return Response({"success": False, "message":e.detail, "errors": e}, status=status.HTTP_403_FORBIDDEN)
