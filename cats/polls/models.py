from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=400, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices')
    text = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.text


class Vote(models.Model):
    poll = models.ForeignKey(Poll, related_name='votes')
    choice = models.ForeignKey(Choice, related_name='choice_votes')

    def __str__(self):
        return self.choice.text
