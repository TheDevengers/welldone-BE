from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, EmailField
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

from users.models import Profile

User = get_user_model()


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email',
                  'username']
        read_only_fields = ['id']


class UserSignUpSerializer(ModelSerializer):
    email = EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user_instance = User.objects.create(**validated_data)
        user_instance.set_password(password)
        user_instance.save()
        return user_instance


class ProfileSerializer(ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = ['id', 'description', 'birth_date', 'birth_place']


class UserSerializer(ModelSerializer):

    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        # u = User.objects.get(username='fsmith')
        # freds_department = u.employee.department
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
