from django.core.management.base import BaseCommand
from studious.models import ProjectPaper
from studious.models import Article

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        vals = ProjectPaper.objects.values('pmcid','doi','journal_title','title','journal_year','int_open_data','int_data_share',)
        papers = vals.distinct().order_by('pmcid')
        objs = (Article(pmcid=i["pmcid"],
        	            doi=i["doi"],
        	            journal_title=i["journal_title"],
        	            title=i["title"],
        	            journal_year=i["journal_year"],
        	            int_open_data=i["int_open_data"],
        	            int_data_share=i["int_data_share"]) for i in papers)

        Article.objects.bulk_create(objs)

        print ("records inserted")






