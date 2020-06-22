from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import OrgSerializer
from .serializers import OrgArticleSerializer
from .serializers import PersonSerializer
from .serializers import PersonArticleSerializer
from .serializers import ProjectPaperSerializer
from .serializers import UniqueJournalSerializer
from .serializers import UniquePISerializer
from .serializers import PersonGraphSerializer
from .serializers import OrgGraphSerializer
from .models import ProjectPaper
from .models import Org
from .models import Person
from django.db.models import Count, Window, F
from django.db.models.functions import RowNumber
from django_filters.rest_framework import DjangoFilterBackend


class ProjectPaperViewSet(viewsets.ModelViewSet):
    queryset = ProjectPaper.objects.all().order_by('pmcid')
    serializer_class = ProjectPaperSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id','contact_pi_project_leader','organization_name','pi_id','org_id','pmcid']
    search_fields = ['id','contact_pi_project_leader','organization_name', 'pmcid']

class OrgArticleViewSet(viewsets.ModelViewSet):
    queryset = ProjectPaper.objects.all().values('pmcid','doi','journal_title','title','journal_year','open_data','data_share','organization_name').distinct().order_by('title')
    serializer_class = OrgArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['org_id']

class PersonArticleViewSet(viewsets.ModelViewSet):
    queryset = ProjectPaper.objects.all().values('id','pmcid','doi','journal_title','title','journal_year','open_data','data_share','contact_pi_project_leader').distinct().order_by('title')
    serializer_class = PersonArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pi_id']

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('full_name')
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id']
    search_fields = ['full_name']

class PersonGraphViewSet(viewsets.ModelViewSet):
    authors = Person.objects.filter(has_three_pubs=True)
    queryset = authors.values('full_name', 'data_score').annotate(index=Window(expression=RowNumber(), order_by=F('data_score').asc()))
    serializer_class = PersonGraphSerializer

class OrgViewSet(viewsets.ModelViewSet):
    queryset = Org.objects.all().order_by('organization_name')
    serializer_class = OrgSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id']
    search_fields = ['organization_name']

class OrgGraphViewSet(viewsets.ModelViewSet):
    orgs = Org.objects.filter(has_three_pubs=True)
    queryset = orgs.values('organization_name', 'data_score').annotate(index=Window(expression=RowNumber(), order_by=F('data_score').asc()))
    serializer_class = OrgGraphSerializer

@api_view(("GET",))
@permission_classes((AllowAny,))
def unique_journals(request):
    queryset = ProjectPaper.countUniqueJournals()
    data = UniqueJournalSerializer(queryset, many=True).data
    return Response(data)

@api_view(("GET",))
@permission_classes((AllowAny,))
def unique_pis(request):
    queryset = ProjectPaper.countUniquePIs()
    data = UniquePISerializer(queryset, many=True).data
    return Response(data)
