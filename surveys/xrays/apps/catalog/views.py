# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm

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


class PatientForm(ModelForm):
    class Meta:
        model = Patient

def patient_item_edit(request, patient_id=None):
    print "Patient edit"
    if patient_id is not None:
        patient = get_object_or_404(Patient, id=patient_id)
    else:
        patient = None

    if request.GET:
        form = PatientForm(request.GET, instance=patient)
        if form.is_valid():
            patient = form.save()
            return redirect(reverse('patient_item', args=[patient.id]))
    else:
        form = PatientForm(instance=patient)
        
    return render(request, "patient_edit_item.html",
                    {'patient': patient, 'form': form })



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


class SpecialistForm(ModelForm):
    class Meta:
        model = Specialist

def doctor_item_edit(request, doctor_id=None):
    print "Specialist edit"
    if doctor_id is not None:
        doctor = get_object_or_404(Specialist, id=doctor_id)
    else:
        doctor = None

    if request.GET:
        form = SpecialistForm(request.GET, instance=doctor)
        if form.is_valid():
            doctor = form.save()
            return redirect(reverse('doctor_item', args=[doctor.id]))
    else:
        form = SpecialistForm(instance=doctor)
        
    return render(request, "doctor_edit_item.html",
                    {'doctor': doctor, 'form': form })




def survey_item(request, survey_id):

    survey = get_object_or_404(Survey, id=survey_id)
    return  render(request, "survey.html",
                    {'survey': survey})


