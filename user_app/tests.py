from django.test import TestCase
from .forms import RegistrationForm


class TestRegisterView(TestCase):
    def setUp(self):
        # Этот метод нужен, чтобы в него выносить общие для всех методов данные
        self.response = self.client.get('/users/register/')

    def test_get_status_code(self):
        # проверяем - отвечает ли страница - статус 200
        self.assertEqual(self.response.status_code, 200)

    def test_get_form(self):
        # есть ли на странице форма регистрации
        context = self.response.context
        form_context_name = 'form'
        self.assertIn(form_context_name, context)

        # проверяем форму, потому что она особенная
        form = context[form_context_name]
        self.assertEqual(type(form), RegistrationForm)
