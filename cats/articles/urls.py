from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . views import ArticleList, ArticleDetail

urlpatterns = [
    url(r'^api-v1/articles/$', ArticleList.as_view()),
    url(r'^api-v1/articles/(?P<pk>[0-9]+)/$', ArticleDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
