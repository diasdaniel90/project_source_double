from django.core.management.base import BaseCommand
from api.source_telegram import main
# Import script here

class Command(BaseCommand):
    def add_arguments(self, parser):
        # parser.add_argument('--name', type=int)
        ...

    def handle(self, *args, **options):
        print('Starting source_telegram daemon')
        # Execute script here
        main()