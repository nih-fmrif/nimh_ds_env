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
    data_score = models.CharField(max_length=5)
    int_open_data = models.IntegerField()
    int_data_share = models.IntegerField()
    int_data_score = models.IntegerField()
    project_id = models.IntegerField()
    contact_pi_project_leader = models.CharField(max_length=50)
    pi_id = models.IntegerField()
    organization_name = models.CharField(max_length=128)
    org_id = models.IntegerField()
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
        return pis

    def countUniqueOrgs():
        vals = ProjectPaper.objects.values('organization_name')
        orgs = vals.distinct().order_by('organization_name')
        return orgs


class Org(models.Model): 
    organization_name = models.CharField(max_length=128)
    has_three_pubs = models.BooleanField()
    count_total_pubs = models.IntegerField()
    count_data_share = models.IntegerField()
    count_data_open = models.IntegerField()
    count_data_total = models.IntegerField()
    data_share_score = models.FloatField()
    data_open_score = models.FloatField()
    data_score = models.FloatField()
    index_by_score = models.IntegerField()

    def __str__(self): 
        return self.organization_name


class Person(models.Model): 
    full_name = models.CharField(max_length=128)
    has_three_pubs = models.BooleanField()
    count_total_pubs = models.IntegerField()
    count_data_share = models.IntegerField()
    count_data_open = models.IntegerField()
    count_data_total = models.IntegerField()
    data_share_score = models.FloatField()
    data_open_score = models.FloatField()
    data_score = models.FloatField()

    def __str__(self): 
        return self.full_name

class Article(models.Model):
    pmcid = models.IntegerField()
    doi = models.CharField(max_length=48)
    journal_title = models.CharField(max_length=64)
    title = models.CharField(max_length=250)
    journal_year = models.SmallIntegerField()
    int_open_data = models.IntegerField()
    int_data_share = models.IntegerField()

    def __str__(self): 
        return self.title

class ArticleUpdate(models.Model): 
    pmcid = models.IntegerField()
    open_data = models.CharField(max_length=5)
    data_share = models.CharField(max_length=5)
    data_statement = models.TextField()
    edit_user = models.CharField(max_length=64)
    edit_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_merged = models.BooleanField()
    
    def __str__(self): 
        return self.pmcid

