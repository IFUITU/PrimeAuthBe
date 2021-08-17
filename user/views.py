from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.contrib.auth.hashers import make_password
# Create your views here.


class UserMe(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, r):
        
        return Response({"user":{
            "username":r.user.username,
            "first_name":r.user.first_name,
            "last_name":r.user.last_name,
            "email":r.user.email
            }})

class Register(APIView):
    
    def post(self, r):
        new_user = UserSerializer(data=r.data)
        if new_user.is_valid():
            user = User.objects.create(
                username=new_user.validated_data['username'],
                password=make_password(new_user.validated_data['password'], None, 'md5'),
                email=new_user.validated_data['email']
                )
            user.save()
            return Response({"ok":True})
        return Response({"ok":False})

