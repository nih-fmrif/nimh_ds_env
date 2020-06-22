from django.core.management.base import BaseCommand
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Count
from studious.models import Org
from studious.models import ProjectPaper

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        orgs = Org.objects.all()

        for o in orgs:
            paper_stats = ProjectPaper.objects.filter(org_id=o.id).values('org_id',
                                                                            'pmcid',
                                                                            'int_data_share',
                                                                            'int_open_data',
                                                                            'int_data_score',
                                                                            'int_data_share',
                                                                            'int_open_data',
                                                                            'int_data_score'
                                                                            ).distinct().aggregate(
                                                                              count_total_pubs=Count('pmcid'),
                                                                              count_data_share=Sum('int_data_share'),
                                                                              count_data_open=Sum('int_open_data'),
                                                                              count_data_total=Sum('int_data_score'),
                                                                              data_share_score=Avg('int_data_share'),
                                                                              data_open_score=Avg('int_open_data'),
                                                                              data_score=Avg('int_data_score'),
                                                                              )

            Org.objects.filter(id=o.id).update(count_total_pubs=paper_stats['count_total_pubs'],
                                                  count_data_share=paper_stats['count_data_share'],
                                                  count_data_open=paper_stats['count_data_open'],
                                                  count_data_total=paper_stats['count_data_total'],
                                                  data_share_score=paper_stats['data_share_score'],
                                                  data_open_score=paper_stats['data_open_score'],
                                                  data_score=paper_stats['data_score']
                                                  )

