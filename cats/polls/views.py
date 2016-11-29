from rest_framework import generics
from rest_framework.response import Response
from . models import Poll, Vote
from . serializers import PollDetailSerializer,VoteCreateSerializer, PollResultSerializer


class PollDetail(generics.RetrieveAPIView):
    serializer_class = PollDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance is None:
            return Response(status=204)
        return Response(serializer.data)

    def get_object(self):
        poll = Poll.objects.filter(is_active=True).first()
        return poll


class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteCreateSerializer


class VoteDetail(generics.RetrieveAPIView):
    serializer_class = PollResultSerializer
    queryset = Poll.objects.all()


