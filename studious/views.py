from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectPaperSerializer
from .serializers import UniqueJournalSerializer
from .models import ProjectPaper
from django.db.models import Count

class ProjectPaperViewSet(viewsets.ModelViewSet):
    queryset = ProjectPaper.objects.all().order_by('pmcid')
    serializer_class = ProjectPaperSerializer

class UniqueJournalViewSet(viewsets.GenericViewSet):
    queryset = ProjectPaper.countUniqueJournals()
    serializer_class = UniqueJournalSerializer