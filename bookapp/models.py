from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    year_published = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

