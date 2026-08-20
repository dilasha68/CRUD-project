from django.test import TestCase
from django.urls import reverse

from .models import BlogModel


class BlogCrudTests(TestCase):
    def test_home_creates_blog_post(self):
        response = self.client.post(
            reverse('home'),
            {'title': 'Test post', 'author': 'Dilasha', 'content': 'Test content'},
        )

        self.assertRedirects(response, reverse('home'))
        self.assertTrue(BlogModel.objects.filter(title='Test post').exists())

    def test_delete_requires_confirmation_post(self):
        post = BlogModel.objects.create(title='Draft', author='Dilasha', content='Draft')

        response = self.client.get(reverse('delete_one', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(BlogModel.objects.filter(id=post.id).exists())

        response = self.client.post(reverse('delete_one', args=[post.id]))
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(BlogModel.objects.filter(id=post.id).exists())
