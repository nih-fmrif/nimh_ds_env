from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    
    class Meta:
        ordering = ('-pmcid',)
    
    def __str__(self): 
        return self.title
