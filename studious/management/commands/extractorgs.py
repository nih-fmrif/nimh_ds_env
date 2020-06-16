from django.core.management.base import BaseCommand
from studious.models import ProjectPaper
from studious.models import Org

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        vals = ProjectPaper.objects.values('organization_name')
        orgs = vals.distinct().order_by('organization_name')
        objs = (Org(organization_name=i["organization_name"]) for i in orgs)

        Org.objects.bulk_create(objs)

        print ("records inserted")

