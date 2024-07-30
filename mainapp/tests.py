from django.test import TestCase

from mainapp.models import Category, Animal


class TestCategory(TestCase):

    def test_some(self):
        self.assertEqual(1, 1)

    def test_str(self):
        category = Category.objects.create(name="some name")
        self.assertEqual(str(category), "some name")


class TestAnimal(TestCase):

    def test_get_category_name(self):
        category = Category.objects.create(name="some name")
        animal = Animal.objects.create(category=category, name="Roni")
        self.assertEqual(animal.get_category_name(), "some name")
