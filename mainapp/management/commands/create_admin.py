from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Fill db with test data"

    def handle(self, *args, **options):
        try:
            User.objects.create_superuser('admin', 'admin@admin.com', 'qwerty')
        except:
            self.stdout.write(self.style.SUCCESS('Already exists'))
        else:
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
