from django.contrib.auth import authenticate, logout

from config.settings import SECRET_KEY

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

import jwt

from .models import User
from .serializers import JoinSerializer, LoginSerializer


class Login(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(username=username, password=password)

            if user is not None:
                token = jwt.encode(
                {"pk": user.pk},
                SECRET_KEY,
                algorithm="HS256",
            )
                return Response({
                    "success": True,
                    "message": f"Welcome {username}",
                    "data":{
                        "token": token
                    },
                    "errors": None}, status=status.HTTP_200_OK)
            else:
                return Response({
                    "success": False,
                    "message": "failed to login, unvalid username or password",
                    "data": None,
                    "errors": None}, status=status.HTTP_401_UNAUTHORIZED)
            
        else: return Response({"success": False,
            "message": "failed to login",
            "data": None,
            "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

  
class LogOut(APIView):

    def post(self, request):
        logout(request)
        return Response({
            "success": True,
            "message": "good bye",
            "data": None,
            "errors": None}, status=status.HTTP_200_OK)


class Join(APIView):
    def post(self,request):
        serializer = JoinSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            User.objects.create_user(username=username, password=password)

            return Response({
                "success": True,
                "message": "Successfully joined",
                "data": None,
                "errors": None,
                }, status=status.HTTP_201_CREATED)
        
        
        return Response({
            "success": False,
            "message": "join failed",
            "data": None,
            "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)