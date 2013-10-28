from django.db import models
from mantid.models import Slugged

class Project(Slugged):
  name = models.CharField(max_length=255)
  info = models.TextField()
  enable_wiki = models.BooleanField()
