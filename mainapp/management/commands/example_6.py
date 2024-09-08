from rest_framework import serializers
from django.core.management.base import BaseCommand
from mainapp.models import Category, Animal, AnimalCard, Food


class Command(BaseCommand):

    def handle(self, *args, **options):
        class CategorySerializer(serializers.ModelSerializer):
            class Meta:
                model = Category
                fields = '__all__'

        class FoodSerializer(serializers.ModelSerializer):
            class Meta:
                model = Food
                fields = '__all__'

        # class AnimalCardSerializer(serializers.ModelSerializer):
        #     class Meta:
        #         model = AnimalCard
        #         fields = ['text']

        class AnimalSerializer(serializers.ModelSerializer):
            # food = serializers.StringRelatedField(many=True)
            food = FoodSerializer(many=True)
            """
                1. StringRelatedField — представляет объект методом __str__.
                2. PrimaryKeyRelatedField — представляет объект его id (используется по умолчанию).
                3. HyperlinkedRelatedField — представляет объект гипперссылкой.
                Обычно она ведёт на страницу detail этого объекта.
                4. SlugRelatedField — позволяет указать несколько полей для отображения объекта.
            """
            category = CategorySerializer()

            class Meta:
                model = Animal
                fields = '__all__'

        class_list = [Animal, Category, AnimalCard, Food]
        for item in class_list:
            item.objects.all().delete()

        family = Category.objects.create(name='Медведь')
        serializer = CategorySerializer(family)
        print(serializer.data, '\n')

        food1 = Food.objects.create(name='Мясо')
        serializer = FoodSerializer(food1)
        print(serializer.data, '\n')

        # animal_card = AnimalCard.objects.create(text='Карточка Медведя')
        # serializer = AnimalCardSerializer(animal_card)
        # print(serializer.data, '\n')

        animal = Animal.objects.create(name='Борис', category=family)
        food2 = Food.objects.create(name='Мед')
        animal.food.add(food1)
        animal.food.add(food2)
        animal.save()
        serializer = AnimalSerializer(animal)
        print(serializer.data)
