from django.core.management.base import BaseCommand
from studious.models import ProjectPaper

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        ProjectPaper.objects.filter(data_share="TRUE").update(int_data_share=1)
        ProjectPaper.objects.filter(open_data="TRUE").update(int_open_data=1)
        print ("import complete")

