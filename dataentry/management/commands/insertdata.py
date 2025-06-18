from django.core.management.base import BaseCommand
from dataentry.models import Student
class Command(BaseCommand):
    help="it will insert the data to the database"
    def handle(self, *args, **options):
        dataset = [
            {'roll_no':1002,'name':'sakthi','age':24},
            {'roll_no':1003,'name':'nandha kumar','age':21},
            {'roll_no':1004,'name':'anand','age':25}
        ]
        for data in dataset:
            student = Student.objects.create(roll_no=data['roll_no'],name=data['name'],age=data['age'])
        #student = Student.objects.create(roll_no=1001,name='kumaran',age=22)
            self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
    
    