from django.db import models
from django.utils import timezone
from django.db.models import Count
from django.contrib.auth.models import User
from postgres_copy import CopyManager

class ProjectPaper(models.Model): 
    
    pmcid = models.IntegerField()
    doi = models.CharField(max_length=48)
    journal_title = models.CharField(max_length=64)
    title = models.CharField(max_length=250)
    journal_year = models.SmallIntegerField()
    open_data = models.CharField(max_length=5)
    data_share = models.CharField(max_length=5)
    project_id = models.IntegerField()
    contact_pi_project_leader = models.CharField(max_length=50)
    organization_name = models.CharField(max_length=128)
    objects = CopyManager()
    
    class Meta:
        ordering = ('-pmcid',)
    
    def __str__(self): 
        return self.title
        
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

    def countUniqueOrgs():
        vals = ProjectPaper.objects.values('organization_name')
        orgs = vals.distinct().order_by('organization_name')
        countedOrgs = orgs.annotate(journal_count=Count('organization_name'))
        return countedOrgs


class Org(models.Model): 
    organization_name = models.CharField(max_length=128)

    def __str__(self): 
        return self.organization_name


class Person(models.Model): 
    full_name = models.CharField(max_length=128)

    def __str__(self): 
        return self.full_name


