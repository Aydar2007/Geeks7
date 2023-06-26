from django.test import TestCase, Client
from django.urls import reverse

from blog.models import Post


class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(title="test", content="test")

    def test_index(self):
        # reverse по имени эндпоинта "index-page" возвращает строку http://127.0.0.1:8000/
        response = self.client.get(reverse("index-page"))
        self.assertTemplateUsed(response, "blog/index.html")
        self.assertEqual(response.status_code, 200)

    def test_get_about(self):
        response = self.client.get(reverse("about-page"))
        self.assertTemplateUsed(response, "blog/about.html")
        self.assertEqual(response.status_code, 200)

    def test_get_contacts(self):
        response = self.client.get(reverse("contacts-page"))
        self.assertTemplateUsed(response, "blog/contacts.html")
        self.assertEqual(response.status_code, 200)

    # def test_post_update(self):
    #     response = self.client.get(reverse("post-update", args=(1,)))
    #     self.assertTemplateUsed(response, "blog/post_update.html")
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_post_delete(self):
    #     response = self.client.get(reverse("post-delete", args=(1,)))
    #     self.assertTemplateUsed(response, "blog/post_delete.html")
    #     self.assertEqual(response.status_code, 200)
