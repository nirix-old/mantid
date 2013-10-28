from django.db import models

class Slugged(models.Model):
  slug = models.CharField(max_length=255)

  class Meta:
    abstract = True
