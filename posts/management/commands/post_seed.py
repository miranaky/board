from datetime import datetime
import random
from django.core.management.base import BaseCommand
from django_seed import Seed

from users.models import User
from posts.models import Post


class Command(BaseCommand):

    """Create user randomly"""

    help = "It seeds the DB with User"

    def handle(self, *args, **options):
        users = User.objects.all().order_by("-id")[:20]
        post_seeder = Seed.seeder()
        post_seeder.add_entity(
            Post,
            100,
            {
                "author": lambda x: random.choice(users),
                "title": lambda x: post_seeder.faker.sentence(nb_words=8, variable_nb_words=False),
                "content": lambda x: post_seeder.faker.paragraph(nb_sentences=5),
            },
        )
        post_seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"50 posts created!"))
