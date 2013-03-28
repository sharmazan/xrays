# Create your views here.
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django import forms
from django.forms import extras

from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.admin.widgets import AdminDateWidget

from xrays.apps.catalog.models import Patient, Specialist, Survey


@login_required
def patients_list(request):
    patients = Patient.objects.all()
    return render(request, "patients-list.html",
                    {'patients': patients})


@login_required
def patient_item(request, patient_id):

    patient = get_object_or_404(Patient, id=patient_id)
    surveys = Survey.objects.filter(patient=patient_id)

    return  render(request, "patient.html",
                    {'patient': patient,
                     'surveys': surveys })


class PatientForm(ModelForm):
    class Meta:
        model = Patient

@login_required
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


@login_required
def doctor_item(request, doctor_id):

    doctor = get_object_or_404(Specialist, id=doctor_id)
    patients = Patient.objects.filter(doctor=doctor_id)

    return  render(request, "doctor.html",
                    {'doctor': doctor,
                     'patients': patients })


class SpecialistForm(ModelForm):
    class Meta:
        model = Specialist

@login_required
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



@login_required
def survey_item(request, survey_id):

    survey = get_object_or_404(Survey, id=survey_id)
    return  render(request, "survey.html",
                    {'survey': survey})



class SurveyForm(ModelForm):
    class Meta:
        model = Survey

@login_required
def survey_item_edit(request, survey_id=None):
    print "Survey edit"
    if survey_id is not None:
        survey = get_object_or_404(Survey, id=survey_id)
    else:
        survey = None

    if request.GET:
        form = SurveyForm(request.GET, instance=survey)
        if form.is_valid():
            survey = form.save()
            return redirect(reverse('survey_item', args=[survey.id]))
    else:
        form = SurveyForm(instance=survey)
        
    return render(request, "survey_edit_item.html",
                    {'survey': survey, 'form': form })

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


def contact_page(request):
    print datetime.date.today
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            print form.cleaned_data
            data = form.cleaned_data
            data['date'] = datetime.datetime.now()
            message = render_to_string ('contact_form_template.txt', data)
            send_mail("Contact from Rentgen", message, data['email'], ["sergey.sharm@gmail.com"])
            # send_mail("Contact from Rentgen", data['text'], data['email'], ["sergey.sharm@gmail.com"])
            return redirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form


    return  render(request, "contact_page.html", {'form': form})

def thanks_page(request):
    return  render(request, "thanks.html")    