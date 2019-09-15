from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.utils.text import slugify

from articles.models import Category, Article


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class ArticleSerializer(ModelSerializer):

    title = serializers.CharField()
    categories = CategorySerializer(many=True)
    state = serializers.CharField()
    slug = serializers.SerializerMethodField('get_slug')
    image = serializers.URLField(required=False, allow_blank=True)

    def get_slug(self, obj):
        return slugify(obj.title)

    class Meta:
        model = Article
        fields = ['id', 'title', 'introduction', 'body', 'categories', 'state', 'slug', 'image']
        read_only_fields = ['id']
        depth = 1

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        article = Article.objects.create(**validated_data)

        categories = []
        for category_data in categories_data:
            obj = Category.objects.get(name=category_data['name'])
            categories.append(obj)
        article.categories.add(*categories)
        return article

