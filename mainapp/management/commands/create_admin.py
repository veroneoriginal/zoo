from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from user_app.models import MyUser


class Command(BaseCommand):
    help = "Fill db with test data"

    def handle(self, *args, **options):
        try:
            MyUser.objects.create_superuser('admin', 'admin@admin.com', 'qwerty')
        except IntegrityError:
            self.stdout.write(self.style.SUCCESS('Already exists'))
        else:
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
