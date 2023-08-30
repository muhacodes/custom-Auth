from django.contrib.auth import authenticate
from account.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# class UserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'name', 'photo', 'password']

#     def get_photo_url(self, user):
#         if user.photo:
#             request = self.context.get('request')
#             if request is not None:
#                 return request.build_absolute_uri(user.photo.url)
#         return None



class UserSerializerModel(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'photo', 'name',  'username', 'address', 'tel', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()
        return user

        
class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


