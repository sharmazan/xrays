from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from xrays.apps.catalog.models import Patient, Specialist, Survey

def index(request):
    return  render(request, "index.html")


