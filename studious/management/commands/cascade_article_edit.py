from django.core.management.base import BaseCommand
from studious.models import ProjectPaper
from studious.models import Article
from studious.models import ArticleUpdate
from studious.models import Org
from studious.models import Person

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        aus = ArticleUpdate.objects.filter(is_merged=False)
        for au in aus:
            int_open_data = 1 if au.open_data == 'TRUE' else 0
            int_data_share = 1 if au.data_share == 'TRUE' else 0
            int_data_score = 1 if int_open_data==1 or int_data_share==1 else 0
            data_score = "TRUE" if int_data_score==1 else "FALSE"

            arts = Article.objects.filter(pmcid=au.pmcid)
            arts.update(int_open_data=int_open_data,
                        int_data_share=int_open_data,
                        )
            pps = ProjectPaper.objects.filter(pmcid=au.pmcid)
            pps.update(open_data=au.open_data,
                        data_share=au.data_share,
                        data_score=data_score,
                        int_open_data=int_open_data,
                        int_data_share=int_data_share,
                        int_data_score=int_data_score
                        )
            print ("updated: "+str(au.pmcid))
        aus.update(is_merged=True)
        print ("updates done")
