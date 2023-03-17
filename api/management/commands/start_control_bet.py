from django.core.management.base import BaseCommand
from api.control_bet import main
# Import script here

class Command(BaseCommand):
    def add_arguments(self, parser):
        # parser.add_argument('--name', type=int)
        ...

    def handle(self, *args, **options):
        print('Starting control_bet daemon')
        # Execute script here
        main()