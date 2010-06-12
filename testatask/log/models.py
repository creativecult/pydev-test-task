from django.db import models
from django.db.models import signals
from django.contrib.contenttypes import models as contenttype_models, generic

class Entry(models.Model):
    ACTION = (
        (1, 'create'),
        (2, 'update'),
        (3, 'delete'),
    )
    timestamp = models.DateTimeField(auto_now_add = True)
    contenttype = models.ForeignKey(contenttype_models.ContentType)
    object_pk = models.PositiveIntegerField()
    action = models.PositiveIntegerField(choices = ACTION)

    object = generic.GenericForeignKey('contenttype', 'object_pk')

def create_entry(instance, action):
    entry = Entry(object = instance, action = action)
    entry.save()

def save_object(sender, instance, created, **kwargs):
    if not isinstance(instance, Entry):
        if created:
            create_entry(instance, 1)
        else:
            create_entry(instance, 2)

def delete_object(sender, instance, **kwargs):
    if not isinstance(instance, Entry):
        create_entry(instance, 3)

signals.post_save.connect(save_object)
signals.post_delete.connect(delete_object)
