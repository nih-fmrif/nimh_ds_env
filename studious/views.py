from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectPaperSerializer
from .models import ProjectPaper
from django.db.models import Count

class ProjectPaperViewSet(viewsets.ModelViewSet):
    queryset = ProjectPaper.objects.all().order_by('pmcid')
    serializer_class = ProjectPaperSerializer
    
    def countUniqueJournals():
        vals = ProjectPaper.objects.values('journal_title')
        journals = vals.distinct().order_by('journal_title')
        countedJournals = journals.annotate(journal_count=Count('journal_title'))
        return countedJournals

    def countUniquePIs():
        vals = ProjectPaper.objects.values('contact_pi_project_leader')
        pis = vals.distinct().order_by('contact_pi_project_leader')
        countedPIs = pis.annotate(pi_count=Count('contact_pi_project_leader'))
        return countedPIs
