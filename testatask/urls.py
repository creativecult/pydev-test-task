from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from registration.forms import RegistrationFormUniqueEmail

urlpatterns = patterns('',
    # Example:
    # (r'^testatask/', include('testatask.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    url(r'^auth/register/$', 'registration.views.register', {'form_class': RegistrationFormUniqueEmail}),
    (r'^auth/', include('registration.urls')),
    (r'^college/', include('college.urls')),
)
