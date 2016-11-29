from rest_framework import generics
from . models import Article
from . serializers import ArticleListSerializer, ArticleDetailSerializer


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.published()
    serializer_class = ArticleListSerializer


class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.published()
    serializer_class = ArticleDetailSerializer




