from rest_framework import serializers
from .models import ProjectPaper
from .models import Org
from .models import Person

class ProjectPaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectPaper
        fields = ('id', 'pmcid','doi', 'journal_title','title','journal_year','open_data','data_share','project_id','contact_pi_project_leader','organization_name','pi_id','org_id')

class OrgArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectPaper
        fields = ('pmcid','doi','journal_title','title','journal_year','open_data','data_share','organization_name',)

class PersonArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectPaper
        fields = ('pmcid','doi','journal_title','title','journal_year','open_data','data_share','contact_pi_project_leader',)

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id','full_name','data_score')

class OrgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Org
        fields = ('id','organization_name','data_score')

class UniqueJournalSerializer(serializers.Serializer):
    journal_title = serializers.CharField(max_length=64)
    journal_count = serializers.IntegerField(max_value=None, min_value=None)

class UniquePISerializer(serializers.Serializer):
    contact_pi_project_leader = serializers.CharField(max_length=64)
    pi_count = serializers.IntegerField(max_value=None, min_value=None)