from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from articles.models import Category, Article


class CategorySerializer(ModelSerializer):

    id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['name']


class ArticleListSerializer(ModelSerializer):

    categories = CategorySerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'introduction', 'author', 'categories', 'image', 'publication_date']


class ArticleSerializer(ModelSerializer):

    categories = CategorySerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'introduction', 'body', 'categories', 'state', 'slug', 'image']
        depth = 1

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        article = Article.objects.create(**validated_data)

        categories = []
        for category_data in categories_data:
            obj = Category.objects.get(id=category_data['id'])
            categories.append(obj)
        article.categories.add(*categories)
        return article

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories', '')

        instance.title = validated_data.get('title', instance.title)
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.body = validated_data.get('body', instance.body)
        instance.state = validated_data.get('state', instance.state)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.image = validated_data.get('image', instance.image)

        categories = []
        for category_data in categories_data:
            try:
                obj = Category.objects.get(id=category_data['id'])
                categories.append(obj)
            except Category.DoesNotExist:
                obj = None

        if categories:
            instance.categories.set(categories)

        instance.save()

        return instance
