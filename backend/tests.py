from django.test import TestCase
from .models import Post

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Test Post", content="This is a test post", created_by="Test User")

    def test_post_content(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.content, "This is a test post")
        self.assertEqual(post.created_by, "Test User")