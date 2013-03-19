from django.contrib import admin
from models import Specialist, Patient, Survey


# class PatientInLine(admin.TabularInline):
#     model = Patient

# class PatientAdmin(admin.ModelAdmin):
# #    list_display = ("name", "date")
#     inlines = ("PatientInLine", )


# admin.site.register(Patient, PatientAdmin)
admin.site.register(Patient)
admin.site.register(Survey)
admin.site.register(Specialist)
