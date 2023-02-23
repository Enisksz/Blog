from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterUserSerializer,ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework import status


from django.contrib.auth.models import User
# Create your views here.

class RegisterUserAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer

class ChangePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
    
    def put(self,request,*args,**kwargs):
        self.object = self.get_object()
      
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get('old_password')
            if not self.object.check_password(old_password):
                return Response({"old_password":"wrong_password"},status=status.HTTP_400_BAD_REQUEST)
            
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            #şifre değiştikten sonra oturumun kapanmamasını sağlar
            update_session_auth_hash(request, self.object)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)