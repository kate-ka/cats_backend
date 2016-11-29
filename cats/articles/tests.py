import json
from django.test import TestCase

# Create your tests here.
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.test import APIClient
from articles.models import Article


class ArticlesTestCase(TestCase):
    client_class = APIClient

    def test_articles_list_returns_200(self):
        # Create article
        article = Article.objects.create(
            title='test',
            content='content',
            short_content='short content',
            image='image_path',
            is_published=True,

        )

        article2 = Article.objects.create(
            title='test2',
            content='content2',
            short_content='short content2',
            image='image_path2',
            is_published=True,

        )

        response = self.client.get(path='/api-v1/articles/')
        self.assertEqual(response.status_code, HTTP_200_OK)

        response_json = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_json), 2)

        fist_article_response = response_json[0]
        self.assertEqual(fist_article_response['title'], 'test')
        self.assertEqual(fist_article_response['shortContent'], 'short content')
        self.assertEqual(fist_article_response['image'], 'http://testserver/media/image_path')
        self.assertNotIn('content', fist_article_response)

        second_article_response = response_json[1]
        self.assertEqual(second_article_response['title'], 'test2')
        self.assertEqual(second_article_response['shortContent'], 'short content2')
        self.assertEqual(second_article_response['image'], 'http://testserver/media/image_path2')
        self.assertNotIn('content', second_article_response)

    def test_articles_list_returns_published_articles_and_status_200(self):

        article = Article.objects.create(
            title='test',
            content='content',
            short_content='short content',
            image='image_path',
            is_published=True,
        )

        article2 = Article.objects.create(
            title='test2',
            content='content2',
            short_content='short content2',
            image='image_path2',
            is_published=False
        )
        response = self.client.get('/api-v1/articles/')
        self.assertEqual(response.status_code, HTTP_200_OK)

        response_json = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_json), 1)
        self.assertEqual(response_json[0]['title'], 'test')
        self.assertEqual(response_json[0]['shortContent'], 'short content')
        self.assertEqual(response_json[0]['image'], 'http://testserver/media/image_path')
        self.assertNotIn('content', response_json[0])

    def test_articles_details_return_valid_details_and_status_200(self):
        article = Article.objects.create(
            title='test',
            content='content',
            short_content='short content',
            image='image_path',
            is_published=True,
        )
        response = self.client.get('/api-v1/articles/{}/'.format(article.id))
        self.assertEqual(response.status_code, HTTP_200_OK)
        response_json = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response_json['title'], 'test')
        self.assertEqual(response_json['content'], 'content')
        self.assertEqual(response_json['image'], 'http://testserver/media/image_path')
        self.assertNotIn('shortContent', response_json)

    def test_nonexistent_article_details_returns_status_404(self):

        response = self.client.get('/api-v1/articles/{}/'.format(666))
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)


    def test_unpublished_article_details_returns_status_404(self):
        article = Article.objects.create(
            title='test',
            content='content',
            short_content='short content',
            image='image_path',
            is_published=False,
        )
        response = self.client.get('/api-v1/articles/{}/'.format(article.id))
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)










