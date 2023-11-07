from django.urls import reverse
from django.test import TestCase
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


class URLsTest(TestCase):

    def test_poem_list_url_ok(self):
        url = reverse('poesias:poema_list')
        self.assertEqual(url, '/poema_list/')
