from django_seed import Seed
from django.core.management.base import BaseCommand
from prices.models import Price 

class Command(BaseCommand):

    help = "This command good"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, type=int, help="How many seed?")

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(Price, number, {
            
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} prices created!'))
        

