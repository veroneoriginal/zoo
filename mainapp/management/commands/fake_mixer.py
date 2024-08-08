from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from mainapp.models import Category, Animal


class Command(BaseCommand):
    help = "Fake data with mixer"

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
        # # использование mixer с lambda-функцией
        # for i in range(5):
        #     category = mixer.blend(Category, name=lambda: f'category{i}')
        #     print(category.name)

        my_list = ["Рыбка", "Свинка", "Крыска"]
        # но можно и без нее (в этом случае)
        for i in my_list:
            category = mixer.blend(Category, name=f'{i}')


