from rest_framework import serializers
from .models import ProjectPaper

class ProjectPaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectPaper
        fields = ('pmcid','doi', 'journal_title','title','journal_year','open_data','data_share','project_id','contact_pi_project_leader','organization_name')