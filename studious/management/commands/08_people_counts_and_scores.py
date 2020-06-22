from django.core.management.base import BaseCommand
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Count
from studious.models import Person
from studious.models import ProjectPaper

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
		people = Person.objects.all()

		for p in people:
			paper_stats = ProjectPaper.objects.filter(pi_id=p.id).aggregate(count_total_pubs=Count('pmcid'),
																			count_data_share=Sum('data_share'),
				                                                            count_data_open=Sum('open_data'),
				                                                            count_data_total=Sum('data_score'),
				                                                            data_share_score=Avg('data_share'),
				                                                            data_open_score=Avg('open_data'),
				                                                            data_score=Avg('data_score'),
				                                                            )

			Person.objects.filter(id=p.id).update(count_total_pubs=paper_stats['count_total_pubs'],
				                                  count_data_share=paper_stats['count_data_share'],
				                                  count_data_open=paper_stats['count_data_open'],
												  count_data_total=paper_stats['count_data_total'],
												  data_share_score=paper_stats['data_share_score'],
												  data_open_score=paper_stats['data_open_score'],
												  data_score=paper_stats['data_score']
												  )

