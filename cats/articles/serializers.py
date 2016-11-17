from rest_framework import serializers
from . models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'short_content', 'image', 'is_featured', 'published_date')


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'image', 'is_featured', 'published_date')