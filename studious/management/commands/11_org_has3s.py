from django.core.management.base import BaseCommand
from studious.models import Org

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Org.objects.filter(count_total_pubs__gte=3).update(has_three_pubs=True)
        print ("tagged orgs with more than 3 pubs")
