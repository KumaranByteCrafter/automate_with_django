from django.core.management.base import BaseCommand
#proposed command = python manage.py greeting kumaran
#proposed output = Hi {name} ,good morning!
class Command(BaseCommand):
    help = 'Greet the User'
    
    def add_arguments(self, parser):
        parser.add_argument('name',type=str,help="sepcifies the user name")
    def handle(self, *args, **kwargs):
        # write a logic
        name = kwargs['name']
        greeting = f'Hi {name} ,good morning!'
        self.stdout.write(self.style.SUCCESS(greeting))