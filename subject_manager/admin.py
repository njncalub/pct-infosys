from django.contrib import admin
from subject_manager.models import Subject, SubjectInstance

class SubjectAdmin(admin.ModelAdmin):
    model = Subject

class SubjectInstanceAdmin(admin.ModelAdmin):
    model = SubjectInstance


admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectInstance, SubjectInstanceAdmin)
