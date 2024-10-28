from rest_framework import serializers
from .models import CustomUser as User

#The user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'name', 'email', 'password', 'role'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            role = validated_data['role'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user