from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
User = get_user_model()

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        # Create user
        user_data = {
            'username':'keiner',
            'password':'1234'
        }
        user1 = User.objects.create(**user_data)

        # create post
        post_data = {
            'author': user1,
            'title':'un nuevo dia',
            'body':'estoy feliz',
        }
        Post.objects.create(**post_data)

    def test_post_content(self):
        post = Post.objects.first()
        author = str(post.author)
        title = post.title
        body = post.body

        self.assertEqual(author, 'keiner')
        self.assertEqual(title, 'un nuevo dia')
        self.assertEqual(body, 'estoy feliz')
