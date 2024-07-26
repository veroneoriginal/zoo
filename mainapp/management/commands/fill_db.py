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
        wolf = Category.objects.create(name='Волк')
        hamster = Category.objects.create(name='Хомяк')
        cat = Category.objects.create(name='Кошка')
        dog = Category.objects.create(name='Собака')

        print('Delete food ... ')
        Food.objects.all().delete()

        print('Create food ... ')
        banana = Food.objects.create(name='Банан')
        meat = Food.objects.create(name='Мясо')
        honey = Food.objects.create(name='Мед')

        print('Create wild animals ... ')
        for _ in range(3):
            leo = WildAnimal.objects.create(name="Leo", category=wolf, age=1)
            tiger_leo = WildAnimal.objects.create(name="Tiger Leo", category=tiger, age=3)
            boris = WildAnimal.objects.create(name="Boris", category=bear, age=5)

        print('check wild animals age')
        for animal in WildAnimal.objects.all():
            print(animal.name, animal.age)

        # many to many - многие ко многим
        leo.food.add(meat)
        leo.food.add(banana)
        leo.save()

        tiger_leo.food.add(meat)
        tiger_leo.save()

        boris.food.add(meat)
        boris.food.add(honey)
        boris.save()

        # увеличить возраст всех животных на 1
        WildAnimal.objects.all().update(age=F('age') + 1)

        # Запрос обновленных значений из базы данных для проверки
        updated_animals = WildAnimal.objects.all()

        print('check wild animals age after update')
        for animal in updated_animals:
            print(f"Wild_animal: {animal.name}, Age: {animal.age}")

        print('Create animals ... ')
        animals_list = []
        for _ in range(10):
            tom = Animal(name="Tom", category=hamster)
            animals_list.append(tom)

            roni = Animal(name="Roni", category=cat)
            animals_list.append(roni)

            johns = Animal(name="Johns", category=dog)
            animals_list.append(johns)

        Animal.objects.bulk_create(animals_list)

        # # всех животных в базе сделать тиграми
        # Animal.objects.all().update(category=tiger)

        # # удаление объектов по фильтру
        # Animal.objects.filter(name="Boris").delete()

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
