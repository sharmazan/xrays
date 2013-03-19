from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'xrays.views.index', name='main_page'),

 
    url(r'^new-patient/$', 'xrays.apps.catalog.views.new_patient'),
    url(r'^new-survey/$', 'xrays.apps.catalog.views.new_survey'),

    # url(r'^xrays/', include('xrays.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:


    url(r'^admin/', include(admin.site.urls), name='admin_panel'),


    # url(r'^patients/', include('xrays.apps.catalog.urls')),
    # url(r'^survey/', include('xrays.apps.catalog.urls')),
    # url(r'^doctors/', include('xrays.apps.catalog.urls')),

    url(r'^patients/$', 'xrays.apps.catalog.views.patients_list', name='patients_list'),
    url(r'^patients/(?P<patient_id>\d+)/$', 'xrays.apps.catalog.views.patient_item', name='patient_item'),

    url(r'^survey/(?P<survey_id>\d+)/$', 'xrays.apps.catalog.views.survey_item', name='survey_item'),

    url(r'^doctors/$', 'xrays.apps.catalog.views.doctors_list', name='doctors_list'),
    url(r'^doctors/(?P<doctor_id>\d+)/$', 'xrays.apps.catalog.views.doctor_item', name='doctor_item'),

    url(r'', include('django.contrib.flatpages.urls')),

)
