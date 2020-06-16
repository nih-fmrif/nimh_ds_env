from rest_framework import serializers
from .models import ProjectPaper

class ProjectPaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectPaper
        fields = ('id', 'pmcid','doi', 'journal_title','title','journal_year','open_data','data_share','project_id','contact_pi_project_leader','organization_name')

class UniqueJournalSerializer(serializers.Serializer):
    journal_title = serializers.CharField(max_length=64)
    journal_count = serializers.IntegerField(max_value=None, min_value=None)

class UniquePISerializer(serializers.Serializer):
    contact_pi_project_leader = serializers.CharField(max_length=64)
    pi_count = serializers.IntegerField(max_value=None, min_value=None)