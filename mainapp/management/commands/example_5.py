from rest_framework import serializers
from mainapp.management.commands.python_models import (Family,
# from python_models import (Family,
                           FamilyCard,
                           Kind,
                           Food)


class FamilySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    max_age = serializers.IntegerField()


class FamilyCardSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1024)
    family = FamilySerializer()


class KindSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    family = FamilySerializer()


class FoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    families = FamilySerializer(many=True)


family1 = Family('Медведь', 50)
serializer = FamilySerializer(family1)
print(serializer.data)
# {'name': 'Медведь', 'max_age': 50}

card = FamilyCard('Текст карточки', family1)
serializer = FamilyCardSerializer(card)
print(serializer.data)
# {'text': 'Текст карточки',
# 'family': {'name': 'Медведь', 'max_age': 50}}

kind = Kind('Бурый', family1)
serializer = KindSerializer(kind)
print(serializer.data)
# {'name': 'Бурый', 'family': {'name': 'Медведь', 'max_age': 50}}

family2 = Family('Тигр', 30)
food = Food('мясо', [family1, family2])
serializer = FoodSerializer(food)
print(serializer.data)
# {'name': 'мясо',
# 'families': [{'name': 'Медведь', 'max_age': 50}, {'name': 'Тигр', 'max_age': 30}]}
