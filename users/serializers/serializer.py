from rest_framework.serializers import ModelSerializer, EmailField
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

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
