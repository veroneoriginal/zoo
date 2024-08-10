from django.core.management.base import BaseCommand
import factory
from mainapp.models import (
    Category,
    Animal
)


class Command(BaseCommand):
    help = "Fake data with mixer"

    Category.objects.all().delete()
    Animal.objects.all().delete()

    def handle(self, *args, **options):
        class CategoryFactory(factory.Factory):
            class Meta:
                model = Category

            name = "Fixed name"

        category = CategoryFactory()
        print(category.name)

        category = CategoryFactory(name="Other name")
        print(category.name)
        print(category.id)
        print(type(category))
