# encoding: utf8

from django import template
from django.core import urlresolvers

register = template.Library()

@register.inclusion_tag('widget/widget.html')
def widget(request, object):
    url = urlresolvers.reverse('admin:%s_%s_change' % (object._meta.app_label, object._meta.module_name), args=[str(object.pk)])
    title = object._meta.verbose_name
    return {'request': request, 'object': object, 'title': title, 'url': url}
