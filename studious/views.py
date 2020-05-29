from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectPaperSerializer
from .models import ProjectPaper


class ProjectPaperViewSet(viewsets.ModelViewSet):
    queryset = ProjectPaper.objects.all().order_by('pmcid')
    serializer_class = ProjectPaperSerializer
