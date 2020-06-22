from django.core.management.base import BaseCommand
from studious.models import ProjectPaper
from studious.models import Org

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        vals = Org.objects.values('id','organization_name')
        orgs = vals.distinct().order_by('id')
        
        for org in orgs:
        	ProjectPaper.objects.filter(organization_name=org['organization_name']).update(org_id=org['id'])

        print ("import complete")

