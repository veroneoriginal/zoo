from django.core.management.base import BaseCommand
from faker import Faker
from mainapp.models import Category


class Command(BaseCommand):
    help = "Fake data with Faker"

    def handle(self, *args, **options):
        # fake = Faker(['it-IT', 'en_US'])
        fake = Faker('ru_RU')
        for i in range(5):
            print(i + 1)
            #
            # name = fake.name()
            # print('name', name)
            #
            # address = fake.address()
            # print('address', address)
            #
            # text = fake.text()
            # print('text', text)

            color = fake.color()
            print('color', color)

            print(Category(name=fake.job()))
