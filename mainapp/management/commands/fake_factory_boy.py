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
        # Объявляю фабрику
        class FirstCategoryFactory(factory.Factory):
            # внутри - описание фабрики
            class Meta:
                model = Category

            # Указываю, как будет заполнено поле - в данном случае оно статичное
            name = "Fixed name"

        # Создаю объект фабрики
        category = FirstCategoryFactory()
        print(category.name)

        # второй вариант - подать атрибут при создании экземпляра класса
        category = FirstCategoryFactory(name="Other name")
        print(category.name)
        print('category.id without ORM - ', category.id)
        print(type(category), '\n')

        # сохранение в базу происходит только в этом случае
        # category.save()

        class SecondCategoryFactory(factory.django.DjangoModelFactory):
            """Для работы с ORM"""

            class Meta:
                model = Category

            name = factory.Faker('name')

        # сохранение в базу по умолчанию
        category = SecondCategoryFactory(name="Измененное имя")
        print(category.name,
              'category.id with ORM -', category.id, '\n')

        # не указывая имя, возьмет name из описания фабрики, сохраняет в базу
        category = SecondCategoryFactory()
        print(category.name,
              'без аргумента, category.id with ORM -', category.id, '\n')

        Category.objects.all().delete()

        # тот же самый результат будет если добавить create
        category = SecondCategoryFactory.create()
        print(category.name,
              'with create -', category.id, '\n')

        # если build - в базе сохранения не будет
        category = SecondCategoryFactory.build()
        print(category.name,
              'with build -', category.id, '\n')

        class AnimalFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = Animal

            name = factory.Faker('name')
            category = factory.SubFactory(SecondCategoryFactory)

        animal = AnimalFactory.create()
        print('animal', animal)
        print('animal.name', animal.name)
        print('animal.category.name', animal.category.name)
