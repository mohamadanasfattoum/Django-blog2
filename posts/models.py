from django.db import models

# Create your models here.

'''
    - html widght
    - validation
    - best for db

'''

class post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=5000)
    publish_date = models.DateTimeField()