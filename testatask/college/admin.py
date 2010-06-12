from django.contrib import admin
from college import models

#admin.site.register(models.Student)
#admin.site.register(models.Group)

class StudentInline(admin.TabularInline):
    model = models.Student

class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline, ]
    
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Student)
