import io
from django.core.management.base import BaseCommand
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from mainapp.management.commands.python_models import Family


class Command(BaseCommand):

    def handle(self, *args, **options):


        class FamilySerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            max_age = serializers.IntegerField()

        # 1. Сериализация в python объект
        family = Family('Медведь', 50)
        serializer = FamilySerializer(family)

        print(serializer.data)
        # {'name': 'Медведь', 'max_age': 50}
        print(type(serializer.data))
        # <class 'rest_framework.utils.serializer_helpers.ReturnDict'>
        # ____________________________________________________________

        renderer = JSONRenderer()
        json_bytes = renderer.render(serializer.data)
        print(json_bytes)
        # b'{"name":"\xd0\x9c\xd0\xb5\xd0\xb4\xd0\xb2\xd0\xb5\xd0\xb4\xd1\x8c","max_age":50}'
        print(type(json_bytes))
        # <class 'bytes'>
        # ____________________________________________________________

        # 2. Нам пришли байты и отправляем пользователю объект
        stream = io.BytesIO(json_bytes)
        data = JSONParser().parse(stream)
        print(data)
        # {'name': 'Медведь', 'max_age': 50}
        print(type(data))
        # <class 'dict'>

        serializer = FamilySerializer(data=data)
        print(serializer.is_valid())
        # True
        print(serializer.validated_data)
        # {'name': 'Медведь', 'max_age': 50}
        print(type(serializer.validated_data))
        # <class 'dict'>
