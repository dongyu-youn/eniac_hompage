from django_seed import Seed
from django.core.management.base import BaseCommand
from doits.models import Doit 
from users import models as user_models
import random

class Command(BaseCommand):

    help = "This command good"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, type=int, help="How many seed?")

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()
        user = user_models.User.objects.all()

        seeder.add_entity(Doit, number, {
            'user': lambda x: random.choice(user)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} prices created!'))
        

