# views
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template

def index(request):
    return  direct_to_template(request, "index.html")

def patients(request):
    return  direct_to_template(request, "patients-list.html")

def new_patient(request):
    return  direct_to_template(request, "new-patient.html")

def new_survey(request):
    return  direct_to_template(request, "new-survey.html")

def patients(request):
    return  direct_to_template(request, "patients-list.html")

