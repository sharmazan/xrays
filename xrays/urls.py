from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'xrays.views.index', name='main_page'),

    # url(r'^xrays/', include('xrays.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:


    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^comments/', include('django.contrib.comments.urls')),


    # url(r'^patients/', include('xrays.apps.catalog.urls')),
    # url(r'^survey/', include('xrays.apps.catalog.urls')),
    # url(r'^doctors/', include('xrays.apps.catalog.urls')),

    url(r'^patients/$', 'xrays.apps.catalog.views.patients_list', name='patients_list'),
    url(r'^patients/(?P<patient_id>\d+)/$', 'xrays.apps.catalog.views.patient_item', name='patient_item'),
    url(r'^patients/(?P<patient_id>\d+)/edit/$', 'xrays.apps.catalog.views.patient_item_edit', name='patient_edit'),
    url(r'^patients/new/$', 'xrays.apps.catalog.views.patient_item_edit', name='patient_create'),

    url(r'^doctors/$', 'xrays.apps.catalog.views.doctors_list', name='doctors_list'),
    url(r'^doctors/(?P<doctor_id>\d+)/$', 'xrays.apps.catalog.views.doctor_item', name='doctor_item'),
    url(r'^doctors/(?P<doctor_id>\d+)/edit/$', 'xrays.apps.catalog.views.doctor_item_edit', name='doctor_edit'),
    url(r'^doctors/new/$', 'xrays.apps.catalog.views.doctor_item_edit', name='doctor_create'),    

    url(r'^survey/(?P<survey_id>\d+)/$', 'xrays.apps.catalog.views.survey_item', name='survey_item'),
    url(r'^survey/(?P<survey_id>\d+)/edit/$', 'xrays.apps.catalog.views.survey_item_edit', name='survey_edit'),
    url(r'^survey/new/$', 'xrays.apps.catalog.views.survey_item_edit', name='survey_create'),

    url(r'^contact/$', 'xrays.apps.catalog.views.contact_page', name='contact_page'),
    url(r'^thanks/$', 'xrays.apps.catalog.views.thanks_page', name='thanks_page'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about_page'),
)
