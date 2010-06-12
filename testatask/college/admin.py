from django.contrib.admin import site
from college import models

site.register(models.Student)
site.register(models.Group)

