from django.db import models

class Specialist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    speciality = models.CharField(max_length=30)
    info = models.TextField()

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    info = models.TextField()
    history = models.TextField(blank=True, null=True)
    doctor = models.ForeignKey(Specialist)

    def __unicode__(self):
    	return "%s %s" % (self.first_name, self.last_name)


class Survey(models.Model):
    patient = models.ForeignKey(Patient)
    date = models.DateTimeField()
    result = models.TextField()
    image = models.ImageField(upload_to="survey-data") #upload_to="d:/survey-data/%s" % (str(self.id))
    technician = models.ForeignKey(Specialist)

    def __unicode__(self):
    	return "%s - %s %s" % (self.date, self.patient.first_name, self.patient.last_name)
