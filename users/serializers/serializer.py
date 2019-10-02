from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, EmailField
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from users.models import Profile

User = get_user_model()


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


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email',
                  'username']
        read_only_fields = ['id']


class ProfileSerializer(ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = ['id', 'description', 'birth_date', 'birth_place']
        read_only_fields = ['id']


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email',
                  'username', 'date_joined']
        read_only_fields = ['id', 'date_joined']

    def validate_email(self, value):
        has_to_check_email = self.instance is not None and self.instance.email != value
        if has_to_check_email and User.objects.filter(email=value).exists():
            raise ValidationError('The email {0} is already used'.format(value))
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.set_password(validated_data.get('password'))
        instance.email = validated_data.get('email')
        instance.save()
        return instance
