from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, EmailField
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from users.models import Profile

User = get_user_model()


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = ['description', 'birth_date', 'birth_place']


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
        Profile.objects.create(user=user_instance)
        return user_instance


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email',
                  'username']
        read_only_fields = ['id']


class UserSerializer(ModelSerializer):

    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email',
                  'username', 'date_joined', 'profile']
        read_only_fields = ['id', 'date_joined']

    def validate_email(self, value):
        has_to_check_email = self.instance is not None and self.instance.email != value
        if has_to_check_email and User.objects.filter(email=value).exists():
            raise ValidationError('The email {0} is already used'.format(value))
        return value

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.description = profile_data.get('description', profile.description)
        profile.birth_date = profile_data.get('birth_date', profile.birth_date)
        profile.birth_place = profile_data.get('birth_place', profile.birth_place)
        profile.save()
        return instance
