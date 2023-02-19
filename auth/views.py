from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from account.models import User
from .serializers import UserSerializer, CustomAuthTokenSerializer
from .authentication import customAuthentication, CustomTokenAuthentication
from django.utils import timezone

class getAllUsers(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})


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
            expiry_time = timezone.now() + timezone.timedelta(minutes=1) # Change this to 2 hours for production
            token.expires = expiry_time
            token.save()

            return Response({'token': token.key, 'expires': expiry_time})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)