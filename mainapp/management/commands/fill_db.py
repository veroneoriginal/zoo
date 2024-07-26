from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Food, Animal, Category, WildAnimal
from django.db.models import F, Q


class Command(BaseCommand):
    help = "Fill db with test data"

    def handle(self, *args, **options):

        print('Delete categories ... ')
        Category.objects.all().delete()

        print('Create categories ... ')
        bear = Category.objects.create(name='Медведь')
        tiger = Category.objects.create(name='Тигр')

        print('Delete food ... ')
        Food.objects.all().delete()

        print('Create food ... ')
        banana = Food.objects.create(name='Банан')
        meat = Food.objects.create(name='Мясо')
        honey = Food.objects.create(name='Мед')

        print('Create animals ... ')

        for _ in range(10):
            leo = WildAnimal.objects.create(name="Leo", category=tiger, age=1)
            tiger_leo = WildAnimal.objects.create(name="Tiger Leo", category=tiger, age=3)
            boris = WildAnimal.objects.create(name="Boris", category=bear, age=5)

        WildAnimal.objects.all().update(age=F('age') + 1)

        wild_animals_list = []
        for _ in range(100):
            leo = Animal(name="Leo", category=tiger)
            wild_animals_list.append(leo)

            tiger_leo = Animal(name="Tiger Leo", category=tiger)
            wild_animals_list.append(tiger_leo)

            boris = Animal(name="Boris", category=bear)
            wild_animals_list.append(boris)

        Animal.objects.bulk_create(wild_animals_list)

        # many to many - многие ко многим
        leo.food.add(meat)
        leo.food.add(banana)
        leo.save()

        tiger_leo.food.add(meat)
        tiger_leo.save()

        boris.food.add(meat)
        boris.food.add(honey)
        boris.save()

        # print('Update ... ')
        # leo.name = "Tom"
        # leo.save()

        # print('Get all ... ')
        # animals = WildAnimal.objects.all()
        # for animal in animals:
        #     print(animal.name)
        #     print(animal.category.name)
        #     for food in animal.food.all():
        #         print(food.name)
        #
        # print('Get one ... ')
        # print('First')
        # first_animal = WildAnimal.objects.filter(id=leo.id).first()
        # print('first_animal =', first_animal.name)
        #
        # print('Get')
        # get_animal = WildAnimal.objects.get(id=leo.id)
        # print('first_animal =', get_animal.name)

        self.stdout.write(
            self.style.SUCCESS('Done')
        )

        # self.stdout.write(
        #     self.style.ERROR('ERROR')
        # )
