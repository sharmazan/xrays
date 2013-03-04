# views
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return  render(request, "index.html")

def patients(request):
#	patients = Patient.objects.all()
    return  render(request, "patients-list.html")

def new_patient(request):
    return  render(request, "new-patient.html")

def new_survey(request):
    return  render(request, "new-survey.html")

def patient(request, patient_id):
    return  render(request, "patient.html")

def survey(request, survey_id):
    return  render(request, "survey.html")

