from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Food, Animal, Category


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
        leo = Animal.objects.create(name="Leo", category=tiger)
        boris = Animal.objects.create(name="Boris", category=bear)

        # many to many - многие ко многим
        leo.food.add(meat)
        leo.food.add(banana)
        leo.save()

        boris.food.add(meat)
        boris.food.add(honey)
        boris.save()

        print('Update ... ')
        leo.name = "Tom"
        leo.save()

        print('Get all ... ')
        animals = Animal.objects.all()
        for animal in animals:
            print(animal.name)
            print(animal.category.name)
            for food in animal.food.all():
                print(food.name)

        print('Get one ... ')
        print('First')
        first_animal = Animal.objects.filter(id=leo.id).first()
        print('first_animal =', first_animal.name)

        print('Get')
        get_animal = Animal.objects.get(id=leo.id)
        print('first_animal =', get_animal.name)


        self.stdout.write(
            self.style.SUCCESS('Done')
        )

        # self.stdout.write(
        #     self.style.ERROR('ERROR')
        # )