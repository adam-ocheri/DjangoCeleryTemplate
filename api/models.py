from django.db import models

# Create your models here.
class JobTracker(models.Model):
    some_property = models.CharField(max_length=50)
    