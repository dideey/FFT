from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from . import models
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        """Handles user login and token generation
            Args: self, request
            Returns: Response
        """
        email = request.data['email']
        password = request.data['password']
        print(email, password)
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
           refresh = RefreshToken.for_user(user)
           return Response({
               'refresh': str(refresh),
                'access': str(refresh.access_token),
           })
        else:
            return Response({
                'error': 'Invalid credentials'
            }, status=400)
    
    @action(detail=False, methods=['POST'], url_path='logout')
    def logout(self, request):
        RefreshToken = request.data['refresh']
        token = RefreshToken(RefreshToken)
        token.blacklist()
        return Response({
            'message': 'Logout successfully'
        })
    permission_classes = (IsAuthenticated)
