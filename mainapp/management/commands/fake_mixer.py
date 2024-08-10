from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from mainapp.models import (
    Category,
    Animal
)


class Command(BaseCommand):
    help = "Fake data with mixer"

    Category.objects.all().delete()
    Animal.objects.all().delete()

    # def handle(self, *args, **options):
    #
    #     category = mixer.blend(Category)
    #     print(category.id, category.name)
    #     print()
    #
    #     animal = mixer.blend(Animal)
    #     print(animal.id)
    #     print(animal.name)
    #     print(animal.category.name)

    def handle(self, *args, **options):
        """ Использование mixer с lambda-функцией """
        # pylint: disable=W0640 cell-var-from-loop
        for i in range(5):
            mixer.blend(Category, name=lambda: f'lambda_func{i}')

        # но можно и без lambda-функции (в этом случае)
        my_list = ["Лошадь", "Собака", "Кошка"]
        for i in my_list:
            mixer.blend(Category, name=f'{i}')

        # генератор
        mixer.cycle(4).blend(Category,
                             name=(name for name in ('Piter', 'John', 'Leo', 'Tom')))

        # Value could be getting a counter
        categories = (mixer.cycle(4).
                      blend(Category,
                            name=mixer.sequence(lambda category: f"category_{category}")
                            ))

        for category in categories:
            print('SEQUENCE', category.name, '\n')

        client = mixer.blend(Animal, name=mixer.RANDOM)
        print('RANDOM', client)

        print(Category.objects.all().values_list('id'), '\n')

        animals = mixer.blend(Animal)
        print("without SELECT", animals.category.id, '\n')

        animals = mixer.blend(Animal, category=mixer.SELECT)
        print(animals.category.id)
