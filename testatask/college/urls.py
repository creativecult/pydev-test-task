from django.conf.urls.defaults import *

urlpatterns = patterns('college.views',
    url(r'^delete/student/(?P<pk>\d+)/$', 'delete_student', name = 'delete-student'),
    url(r'^update/student/(?P<pk>\d+)/$', 'update_student', name = 'update-student'),
    url(r'^create/student/$', 'create_student', name = 'create-student'),
    url(r'^delete/group/(?P<pk>\d+)/$', 'delete_group', name = 'delete-group'),
    url(r'^update/group/(?P<pk>\d+)/$', 'update_group', name = 'update-group'),
    url(r'^create/group/$', 'create_group', name = 'create-group'),
    url(r'^groups/$', 'list_groups', name = 'list-groups'),
    url(r'^(?P<pk>\d+)/$', 'retrieve_group', name = 'retrieve-group'),
)
