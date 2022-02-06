from rest_framework import serializers
from .models import Bucketlist
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified', 'owner')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],

        )
        user.set_password(validated_data['password'])
        user.save()
        # Token.objects.create(user=user)
        print('token utworzony')
        # print('user token \n ', user.auth_token.key)
        return user


# class UserBasicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name']