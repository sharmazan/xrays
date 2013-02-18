from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'xrays.views.index'),
    url(r'^patients/$', 'xrays.views.patients'),
    url(r'^new-patient/$', 'xrays.views.new_patient'),
    url(r'^new-survey/$', 'xrays.views.new_survey'),
    url(r'^patients/(?P<patient_id>\d+)/$', 'xrays.views.patient'),
    url(r'^survey/(?P<survey_id>\d+)/$', 'xrays.views.survey'),
 

    # url(r'^xrays/', include('xrays.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
