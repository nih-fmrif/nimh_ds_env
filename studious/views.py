from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import OrgSerializer
from .serializers import PersonSerializer
from .serializers import ProjectPaperSerializer
from .serializers import UniqueJournalSerializer
from .serializers import UniquePISerializer
from .models import ProjectPaper
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

class ProjectPaperViewSet(viewsets.ModelViewSet):
    queryset = ProjectPaper.objects.all().order_by('pmcid')
    serializer_class = ProjectPaperSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id','contact_pi_project_leader','organization_name']
    search_fields = ['id','contact_pi_project_leader','organization_name']

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('full_name')
    serializer_class = PersonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']

class OrgViewSet(viewsets.ModelViewSet):
    queryset = Org.objects.all().order_by('pmcid')
    serializer_class = OrgSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['organization_name']

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