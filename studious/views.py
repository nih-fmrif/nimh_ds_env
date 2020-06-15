from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectPaperSerializer
from .serializers import UniqueJournalSerializer
from .serializers import UniquePISerializer
from .models import ProjectPaper
from django.db.models import Count

class ProjectPaperViewSet(viewsets.ModelViewSet):
    queryset = ProjectPaper.objects.all().order_by('pmcid')
    serializer_class = ProjectPaperSerializer


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