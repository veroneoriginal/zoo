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


        self.stdout.write(
            self.style.SUCCESS('Done')
        )

        # self.stdout.write(
        #     self.style.ERROR('ERROR')
        # )