from django.db import models
from django.contrib.postgres.fields import ArrayField


class Author(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    born_date = models.DateField(null=False)
    born_location = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=5900, null=False)



class Quote(models.Model):
    tags = ArrayField(models.CharField(max_length=200, null=False))
    author = models.ForeignKey(Author, to_field='id', on_delete=models.CASCADE)
    quote = models.CharField(max_length=999, null=False)