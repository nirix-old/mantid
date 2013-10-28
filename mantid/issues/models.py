from django.db import models
from mantid.models import Slugged
from mantid.projects.models import Project

class Type(models.Model):
  name = models.CharField(max_length=255)
  bullet = models.CharField(max_length=255)

class Status(models.Model):
  name = models.CharField(max_length=255)
  is_closed = models.BooleanField()
  project = models.ForeignKey(Project)

class Milestone(Slugged):
  name = models.CharField(max_length=255)

class Issue(models.Model):
  summary = models.CharField(max_length=255)
  description = models.TextField()
  project = models.ForeignKey(Project)
  user = models.ForeignKey("auth.User")
  milestone = models.ForeignKey(Milestone)
  version_id = models.IntegerField(max_length=11)
  status = models.ForeignKey(Status)
  type = models.ForeignKey(Type)
