from django.db import models

class Catalog(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)\

    def __unicode(self):
    	return "%s %s" % (self.firstname, self.lastname)