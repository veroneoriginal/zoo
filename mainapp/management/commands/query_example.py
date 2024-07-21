from django.core.management.base import BaseCommand
from mainapp.models import WildAnimal, Animal, Category


class Command(BaseCommand):
    help = "Query examples"

    def handle(self, *args, **options):
        print('All animals')
        animals = Animal.objects.all()

        # for animal in animals:
        #     print(animal.name)

        print('Simple filter')
        # Все животные с именем Leo
        leos = Animal.objects.filter(name="Leo")
        # print(len(leos))
        # print(type(leos))
        # print(leos.first().name)

        print('Age animals')
        # Найти животное с возрастом меньше 5 лет
        age_animals = WildAnimal.objects.filter(age__lt=5)

        # for item in age_animals:
        #     print(item.name, item.age)

        # # Найти животное с возрастом меньше или равным 5 лет
        # age_animals = Animal.objects.filter(age__lte=5)
        #
        # # Найти животное с возрастом больше 5 лет
        # age_animals = Animal.objects.filter(age__gt=5)

        print("Animals with name filter")
        # Найти животное, у которого имя содержит Leo с учетом регистра и без
        animals = Animal.objects.filter(name__contains='Leo')
        for item in animals:
            print(item.name)

        # Найти животных с категорией, название которой начинается на Т
        print("Animals with category start T")
        t_category = Category.objects.filter(name__startswith='Т')
        print(t_category)

        # а теперь выводим конкретных животных этой категории
        animals = Animal.objects.filter(category=t_category.first())
        print(animals)

        # теперь можно написать этот запрос в 1 строчку
        animals = Animal.objects.filter(category__name__startswith='Т')
        print(animals)

        # Количество животных
        # не очень хороший вариант
        print(len(animals))

        # хороший вариант
        print(animals.count())

        # есть ли животное с именем содержащим Tom
        animals = Animal.objects.filter(name__icontains='Leo')

        print(animals.exists())
