from django.core.management.base import BaseCommand
from django_seed import Seed

from users.models import User


class Command(BaseCommand):

    """Create user randomly"""

    help = "It seeds the DB with User"

    def handle(self, *args, **options):
        user_seeder = Seed.seeder()
        user_seeder.add_entity(User, 30, {"is_staff": False, "is_superuser": False})
        user_seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"20 users created!"))
