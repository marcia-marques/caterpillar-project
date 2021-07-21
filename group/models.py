from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30) 
    description = models.CharField(max_length=200)
