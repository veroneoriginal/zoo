from django.test import TestCase
from mixer.backend.django import mixer
from mainapp.models import Category, Animal


class TestCategory(TestCase):
    """ Проверка правильности реализации метода преобразования объекта модели Category в строку"""

    def test_name_category_is_str(self):
        category = Category.objects.create(name="some name")
        self.assertEqual(str(category), "some name")


class TestAnimal(TestCase):

    def test_get_category_name(self):
        """ Проверка правильности работы метода get_category_name() у объекта Animal.
             Возвращает ли он имя связанной категории """

        # способ №1
        # category = Category.objects.create(name="some name")
        # animal = Animal.objects.create(category=category, name="Roni")

        # способ №2
        # category = mixer.blend(Category, name="some name")
        # animal = mixer.blend(Animal, category=category)

        # способ №3
        animal = mixer.blend(Animal, category__name="some name")
        self.assertEqual(animal.get_category_name(), "some name")


class TestCategoryListView(TestCase):

    def test_status_code(self):
        """Проверяем отвечаем ли страница"""

        url = '/category/list/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        """Проверка, что представление (view) возвращает список категорий,
         и что этот список корректно обновляется при добавлении новой категории"""

        url = '/category/list/'
        response = self.client.get(url)
        context = response.context
        self.assertIn('object_list', context)
        category_list = context['object_list']
        self.assertEqual(len(category_list), 0)

        Category.objects.create(name="some name")
        response = self.client.get(url)
        context = response.context
        category_list = context['object_list']
        self.assertEqual(len(category_list), 1)

    def test_content(self):
        """Проверка, что контент (текст "some name") присутствует в HTML-ответе,
         возвращаемом представлением на определенном URL"""

        Category.objects.create(name="some name")
        url = '/category/list/'
        response = self.client.get(url)
        self.assertContains(response, "some name", 1)
