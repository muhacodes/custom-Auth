from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import MethodNotAllowed

from account.models import User  # Assuming your User model is in the same directory
from .serializers import (
    UserSerializerModel,
    CustomAuthTokenSerializer,
)
from .authentication import customAuthentication, CustomTokenAuthentication


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerModel
    # permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed("POST")



class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    @csrf_exempt
    def post(self, request, format=None):
        serializer = UserSerializerModel(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ApiLogin(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    authentication_classes = (CustomTokenAuthentication, )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = customAuthentication().authenticate(request, username=serializer.validated_data['email'], password=serializer.validated_data['password'])
        
        if user:
            # Delete any existing tokens for the user
            Token.objects.filter(user=user).delete()

            # Create a new token for the user with an expiry time
            token = Token.objects.create(user=user)
            expiry_time = timezone.now() + timezone.timedelta(minutes=30)  # Change this to 2 hours for production
            token.expires = expiry_time
            token.save()

            user_data = UserSerializerModel(user).data

            return Response({'user': user_data, 'token': token.key, 'expires': expiry_time})
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
