from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import KeySerializer

from .models import Key

import openai


## 1. user는 request에서 가져온다 

class Keys(APIView): 
    """
    유저가 가진 모든 Key를 가져옵니다.
    """
    def verify_api_key(self, api_key):
          client = openai.OpenAI(api_key=api_key)
          try:
              client.models.list()
          except openai.AuthenticationError:
              return False
          else:
              return True

    def get(self, request):
        keys = Key.objects.get(user_id=request.user.id)
        
        if keys:
            return Response({"success":True,
                "message": "chat bot api keys",},
                status=status.HTTP_200_OK)
    
    
    def post(self,request):
        serializer = KeySerializer(request.data);
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            api_key = serializer.validated_data["api_key"]
            kind = serializer.validated_data["kind"]
            
            is_valid_key = self.verify_api_key(api_key=api_key)

            if is_valid_key:
                selected_key = Key.objects.filter(is_selected=True)
                is_selected = True
                if selected_key:
                    is_selected = False        
                Key.objects.create(name=name, api_key=api_key, kind=kind, is_valid=True, is_selected=is_selected)
    
            return Response({"success":True,
                "message": "valid api key",},
                status=status.HTTP_201_CREATED)
    


class AKey(APIView):
    def delete(self,request, pk):
        key = Key.objects.get(id=pk)
        if request.user.id != key.user_id:
            return False
        return True
    

class StaticsAndCharged(APIView):
    def get(self,request, pk):
        return
