from rest_framework import serializers
from . models import Poll, Vote, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text')


class PollDetailSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Poll

        fields = ('id', 'question', 'choices')


class VoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('poll', 'choice')


class ChoiceWithResultsSerializer(serializers.ModelSerializer):
    results = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = ('text', 'results', 'id')

    def get_results(self, choice):
        return Vote.objects.filter(choice=choice).count()


class PollResultSerializer(serializers.ModelSerializer):
    choices = ChoiceWithResultsSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('choices', 'id', 'question')


