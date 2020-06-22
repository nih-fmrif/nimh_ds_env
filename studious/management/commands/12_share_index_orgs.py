from django.core.management.base import BaseCommand
from studious.models import Org

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        vals = Org.objects.values('id','organization_name','index_by_score')
        orgs = vals.order_by('index_by_score')
        
        count = 0
        for org in orgs:
        	count += 1
        	Org.objects.filter(id=org['id']).update(index_by_score=count)

        print ("import complete")