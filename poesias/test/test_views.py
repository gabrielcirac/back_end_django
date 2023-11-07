from django.test import TestCase
from django.urls import reverse, resolve
from poesias import views

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


class ViewsTests(TestCase):
    def test_home_view_is_correct(self):
        view = resolve(reverse('poesias:sobre'))
        self.assertIs(view.func, views.sobre_view)

    def test_user_view_is_correct(self):
        view = resolve(reverse(
            'poesias:user', kwargs={'username': 'Gabriel'}))
        self.assertIs(view.func, views.user_view)

    def test_poema_id_view_is_correct(self):
        view = resolve(
            reverse('poesias:poema_text', kwargs={'poema_id': 2}))
        self.assertIs(view.func, views.poema_text)

    def test_search_view_returns_search_template(self):
        # Utiliza o cliente de teste para fazer uma requisição
        # GET para a URL nomeada 'search'.
        response = self.client.get(reverse('poesias:search'))

        # Verifica se a resposta utiliza o template esperado 'search.html'.
        self.assertTemplateUsed(response, 'search.html')
