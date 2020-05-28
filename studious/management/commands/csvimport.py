from studious.models import ProjectPaper
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)
        insert_count = ProjectPaper.objects.from_csv(
            "./data.csv",
            dict(pmcid="pmcid",
                doi="doi",
                journal_title="journal_title",
                title="title",
                journal_year="journal_year",
                open_data="open_data",
                data_share="data_share",
                project_id="project_id",
                contact_pi_project_leader="contact_pi_project_leader",
                organization_name="organization_name"
                )
            )
        print "{} records inserted".format(insert_count)


$ python manage.py myimportcommand
