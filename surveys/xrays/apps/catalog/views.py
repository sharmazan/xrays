# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from xrays.apps.catalog.models import Patient, Specialist, Survey



def patients_list(request):
    patients = Patient.objects.all()
    return render(request, "patients-list.html",
                    {'patients': patients})



def patient_item(request, patient_id):

    patient = get_object_or_404(Patient, id=patient_id)
    surveys = Survey.objects.filter(patient=patient_id)

    return  render(request, "patient.html",
                    {'patient': patient,
                     'surveys': surveys })


def doctors_list(request):
    doctors = Specialist.objects.all()
    return render(request, "doctors-list.html",
                    {'doctors': doctors})



def doctor_item(request, doctor_id):

    doctor = get_object_or_404(Specialist, id=doctor_id)
    patients = Patient.objects.filter(doctor=doctor_id)

    return  render(request, "doctor.html",
                    {'doctor': doctor,
                     'patients': patients })


def survey_item(request, survey_id):

    survey = Survey.objects.get(id=survey_id)
    return  render(request, "survey.html",
                    {'survey': survey})



def new_patient(request):
    return  render(request, "new-patient.html")


def new_survey(request):
    return  render(request, "new-survey.html")