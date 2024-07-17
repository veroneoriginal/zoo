from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from mainapp.models import Animal, HomeAnimal


class Command(BaseCommand):
    help = "Get all animals"

    def handle(self, *args, **options):
        # Если нужны все животные
        animals = Animal.objects.all()
        for animal in animals:
            print(animal.name)

        print()
        print('next - HOME animals')
        # Если нужны животные из какой-то категории
        animals = HomeAnimal.objects.all()
        for animal in animals:
            print(animal.category)
