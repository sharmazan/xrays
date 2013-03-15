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


    url(r'^patients/', include('xrays.apps.catalog.urls')),
    url(r'^survey/', include('xrays.apps.catalog.urls')),
    url(r'^doctors/', include('xrays.apps.catalog.urls')),

)
