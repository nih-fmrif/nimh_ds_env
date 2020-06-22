from django.core.management.base import BaseCommand
from studious.models import ProjectPaper
from studious.models import Person

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        vals = ProjectPaper.objects.values('contact_pi_project_leader')
        people = vals.distinct().order_by('contact_pi_project_leader')
        objs = (Person(full_name=i["contact_pi_project_leader"]) for i in people)

        Person.objects.bulk_create(objs)

        print ("records inserted")

