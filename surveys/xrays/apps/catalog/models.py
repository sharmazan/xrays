from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    info = TextField()
    history = TextField()
    doctor = ForeignKey(Specialist)

    def __unicode(self):
    	return "%s %s" % (self.firstname, self.lastname)


class Survey(models.Model):
    patient = models.ForeignKey(Patient)
    date = models.DateTimeField('date of survey')
    result = models.TextField()
    specialist = ForeignKey(Specialist)

    def __unicode(self):
    	return "%d - %s %s" % (self.date, patient.firstname, patient.lastname)


class Specialist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    info = TextField()

    def __unicode(self):
    	return "%s %s" % (self.firstname, self.lastname)