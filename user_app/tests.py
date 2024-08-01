from django.test import TestCase
from .forms import RegistrationForm
from .models import MyUser


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


class TestRegisterViewPost(TestCase):

    def setUp(self):
        data = {
            'username': 'new_user',
            'email': 'test@test.ru',
            'password1': 'qweRty_1Nv',
            'password2': 'qweRty_1Nv',
        }
        self.responce = self.client.post('/users/register/', data)

    def test_post_status_code(self):
        # Этот тест проверяет статус-код ответа, который возвращается
        # при попытке отправки POST-запроса на URL /users/register/
        # с определенными данными для регистрации пользователя.

        self.assertEqual(self.responce.status_code, 302)

    def test_user_created(self):
        # Проверяем, что пользователь создан
        self.assertTrue(MyUser.objects.filter(username='new_user').exists())
