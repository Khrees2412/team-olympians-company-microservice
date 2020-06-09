from django.db import models

# Create your models here.
class CompanyList (models.Model):
    name = models.CharField(max_length=50);
    desc = models.CharField(max_length=50);