from django.test import TestCase
from mainapp.models import Category, Animal


class TestCategory(TestCase):

    def test_name_category_is_str(self):
        category = Category.objects.create(name="some name")
        self.assertEqual(str(category), "some name")


class TestAnimal(TestCase):

    def test_get_category_name(self):
        category = Category.objects.create(name="some name")
        animal = Animal.objects.create(category=category, name="Roni")
        self.assertEqual(animal.get_category_name(), "some name")


class TestCategorylistView(TestCase):

    def test_status_code(self):
        url = '/category/list/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
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
        Category.objects.create(name="some name")
        url = '/category/list/'
        response = self.client.get(url)
        self.assertContains(response, "some name", 1)
