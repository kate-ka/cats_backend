from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api-v1/polls/active/$', views.PollDetail.as_view()),
    url(r'^api-v1/votes/$', views.VoteCreate.as_view()),
    url(r'^api-v1/polls/(?P<pk>[0-9]+)/results/$', views.VoteDetail.as_view()),


]

