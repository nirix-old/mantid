from django.http import HttpResponse
from django.template import RequestContext, loader

from mantid.projects.models import Project

def index(request):
  projects = Project.objects.order_by('name')
  template = loader.get_template('projects/index.html')
  context = RequestContext(request, {
    'projects': projects
  })
  return HttpResponse(template.render(context))
