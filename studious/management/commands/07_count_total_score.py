from django.core.management.base import BaseCommand
from studious.models import ProjectPaper

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        ProjectPaper.objects.filter(int_data_share=1).update(int_data_score=1)
        ProjectPaper.objects.filter(int_open_data=1).update(int_data_score=1)
        print ("data scores merged")

