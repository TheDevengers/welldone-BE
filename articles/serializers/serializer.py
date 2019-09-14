from rest_framework.serializers import ModelSerializer
from articles.models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']