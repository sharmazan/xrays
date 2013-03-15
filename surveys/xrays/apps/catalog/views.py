# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from xrays.apps.catalog.models import Patient, Specialist, Survey



def patients(request):
    patients = Patient.objects.all()
    return render(request, "patients-list.html",
                    {'patients': patients})

def new_patient(request):
    return  render(request, "new-patient.html")


def new_survey(request):
    return  render(request, "new-survey.html")


def patient(request, patient_id):

    patient = get_object_or_404(Patient, id=patient_id)
    surveys = Survey.objects.filter(patient=patient_id)

    return  render(request, "patient.html",
                    {'patient': patient,
                     'surveys': surveys })


def survey(request, survey_id):

    survey = Survey.objects.get(id=survey_id)
    return  render(request, "survey.html",
                    {'survey': survey})

