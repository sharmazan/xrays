from django.contrib import admin
from apps.catalog.models import Specialist, Patient, Survey


admin.site.register(Patient)
admin.site.register(Survey)
admin.site.register(Specialist)
