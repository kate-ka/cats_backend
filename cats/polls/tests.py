import json
from django.test import TestCase

# Create your tests here.
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, HTTP_201_CREATED
from rest_framework.test import APIClient
from . models import Poll, Choice
from polls.models import Vote


class PollTestCase(TestCase):
    client_class = APIClient

    def retrieve_latest_active_poll(self):
        # Create article
        poll = Poll.objects.create(
            question='Why???',
            is_active=True

        )
        choice1 = Choice.objects.create(
            poll=poll,
            text='Choice1'

        )
        choice2 = Choice.objects.create(
            poll=poll,
            text='Choice2'

        )
        poll2 = Poll.objects.create(
            question='What???',
            is_active=False

        )
        choice = Choice.objects.create(
            poll=poll2,
            text='Choice2'

        )
        response = self.client.get(path='/api-v1/polls/active')
        self.assertEqual(response.status_code, HTTP_200_OK)
        active_poll_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(active_poll_response), 3)
        self.assertEqual(active_poll_response['question'], 'Why???')
        self.assertEqual(len(active_poll_response['choices']), 2)
        self.assertNotIn(poll2, active_poll_response)

        # Check that choice contains id
        self.assertIn('id', active_poll_response['choices'[0]])

    def test_retrieve_nothing_and_204_when_no_active_poll(self):
        poll_1 = Poll.objects.create(
            question='Why???',
            is_active=False

        )
        poll_2 = Poll.objects.create(
            question='Why???',
            is_active=False

        )
        response = self.client.get(path='/api-v1/polls/active')
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_create_vote_returns_201(self):
        """
        Check that first choice was selected
        and stored in db
        """
        poll = Poll.objects.create(
            question='Why???',
            is_active=True

        )

        choice1 = Choice.objects.create(
            poll=poll,
            text='Choice1'

        )
        choice2 = Choice.objects.create(
            poll=poll,
            text='Choice2'

        )

        data = {
            'poll': poll.id,
            'choice': choice1.id
        }

        response = self.client.post('/api-v1/votes/', data=data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

        # Check db
        self.assertTrue(Vote.objects.filter(poll=poll, choice=choice1))
        
    def test_retrieve_vote_results_returns_200(self):
        poll = Poll.objects.create(
             question='Why???',
            is_active=True
        )
        choice = Choice.objects.create(
            poll=poll,
            text='Choice'

        )
        vote = Vote.objects.create(
            poll=poll,
            choice=choice
        )
        response = self.client.get('/api-v1/polls/' + str(poll.id) +'/results/')
        response_json = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response_json['choices']), 1)
        self.assertEqual(response_json['choices'][0]['text'], 'Choice')
