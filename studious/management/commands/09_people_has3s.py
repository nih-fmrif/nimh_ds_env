from django.core.management.base import BaseCommand
from studious.models import Person

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Person.objects.filter(count_total_pubs>=3).update(has_three_pubs=True)
        print ("tagged users with more than 3 pubs")
