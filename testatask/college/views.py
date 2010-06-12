from django.core import urlresolvers
from django import shortcuts
from django.views.generic import list_detail, create_update
from django.contrib.auth import decorators
from college import models

@decorators.login_required
def delete_student(request, pk):
    student = shortcuts.get_object_or_404(models.Student, pk = pk)
    return create_update.delete_object(request, model = models.Student, object_id = pk, post_delete_redirect = urlresolvers.reverse('retrieve-group', args=[str(student.group.pk)]))

@decorators.login_required
def update_student(request, pk):
    return create_update.update_object(request, model = models.Student, object_id = pk)

@decorators.login_required
def create_student(request):
    return create_update.create_object(request, model = models.Student)

@decorators.login_required
def delete_group(request, pk):
    return create_update.delete_object(request, model = models.Group, object_id = pk, post_delete_redirect = urlresolvers.reverse('list-groups'))

@decorators.login_required
def update_group(request, pk):
    return create_update.update_object(request, model = models.Group, object_id = pk)

@decorators.login_required
def create_group(request):
    return create_update.create_object(request, model = models.Group)

def list_groups(request):
    return list_detail.object_list(request, queryset = models.Group.objects.all())

def retrieve_group(request, pk):
    return list_detail.object_detail(request, queryset = models.Group.objects.all(), object_id = pk)
