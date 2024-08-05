from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Fake data with Faker"

    def handle(self, *args, **options):
        print("ok")
