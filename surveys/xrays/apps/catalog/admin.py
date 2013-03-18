from django.contrib import admin
from models import Specialist, Patient, Survey


class SurveyAdmin(admin.ModelAdmin):
    list_display = ("patient", "date")


admin.site.register(Patient)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Specialist)
