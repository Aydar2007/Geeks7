from django.test import TestCase, Client
from django.urls import reverse


class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        # reverse по имени эндпоинта "index-page" возвращает строку http://127.0.0.1:8000/
        response = self.client.get(reverse("index-page"))

        self.assertEqual(response.status_code, 200)

    def test_get_about(self):
        response = self.client.get(reverse("about-page"))

        self.assertEqual(response.status_code, 200)

    def test_get_contacts(self):
        response = self.client.get(reverse("contacts-page"))

        self.assertEqual(response.status_code, 200)


    def test_contacts_rending(self):
        response = self.client.get(reverse("contacts-page"))
        self.assertTemplateUsed(response,"blog/contacts.html")
        self.assertEqual(response.status_code, 200)

    def test_about_rending(self):
        response = self.client.get(reverse("about-page"))
        self.assertTemplateUsed(response,'blog/about.html')
        self.assertEqual(response.status_code, 200)
    
    def test_index_rending(self):
        response = self.client.get(reverse("index-page"))
        self.assertTemplateUsed(response,"blog/index.html")
        self.assertEqual(response.status_code, 200)