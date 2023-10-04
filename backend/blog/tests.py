from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

## useful for debug
# import pdb
# pdb.set_trace()

class BlogTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

        # Creating users
        user1_data = {
            'username':'keiner',
            'password':'1234'
        }
        user2_data = {
            'username':'mendoza',
            'password':'5678'
        }

        cls.user1 = User.objects.create(**user1_data)
        cls.user2 = User.objects.create(**user2_data)

        # creating posts
        post1_data = {
            'author': cls.user1,
            'title':'un nuevo dia',
            'body':'estoy feliz',
        }
        post2_data = {
            'author': cls.user2,
            'title':"I'm testing",
            'body':"I'm triying to make a test",
        }

        cls.post1 = Post.objects.create(**post1_data)
        cls.post2 = Post.objects.create(**post2_data)


    def test_post_content(self):
        """Test the creation of posts works"""

        post = Post.objects.get(title='un nuevo dia')
        author = str(post.author)
        title = post.title
        body = post.body

        self.assertEqual(post.author, self.user1)
        self.assertEqual(author, 'keiner')
        self.assertEqual(title, 'un nuevo dia')
        self.assertEqual(body, 'estoy feliz')

    def test_api_get_list_post(self):
        """users can read the list of all posts without credentials"""

        response = self.client.get('/api/v1/')

        self.assertContains(response, self.post1)
        self.assertContains(response, self.post2)

    def test_api_get_detail_post(self):
        """users can read a particular post without credentials"""
        
        endpoint = self.post1.get_absolute_url()
        response = self.client.get(endpoint)

        self.assertContains(response, self.post1)

    def test_delete_post_fail_without_token(self):
        """users cannot delete a post without credentials
        at the end the 2 post still the same 
        and response get status 403"""

        post = Post.objects.get(author__username='keiner')
        endpoint = post.get_absolute_url()
        response = self.client.delete(endpoint)

        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_delete_own_post_succefully_with_token(self):
        """users can delete it's own post using it's token
        at the end the count posts decresse
        and the response get status 204"""


        # token and post bellows to the same user
        token = Token.objects.get(user__username='keiner')
        post = Post.objects.get(author__username='keiner')

        # something like this: 
        # DELETE http://127.0.0.1:8000/api/v1/2/ 'Authorization: Token 9d78b3sadfasdfafdgsdfgssdfgdsfsd'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        endpoint = post.get_absolute_url()
        response = self.client.delete(endpoint)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 1)
        
    def test_delete_post_from_other_user_fail(self):
        """users cannot delete post from other user, even providing a valid token
        at the end the count posts decresse
        and the response get status 204"""

        # token and post bellows to the DIFFERENT users
        token = Token.objects.get(user__username='keiner')
        post = Post.objects.get(author__username='mendoza')

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        endpoint = post.get_absolute_url()
        response = self.client.delete(endpoint)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.count(), 2)

