from django.contrib import admin
from subject_manager.models import Subject, SubjectInstance


class SubjectAdmin(admin.ModelAdmin):
    model         = Subject
    list_display  = ('code', 'name', 'units', )
    list_filter   = ('units', )
    search_fields = ('code', 'name', 'description', 'units', )


class SubjectInstanceAdmin(admin.ModelAdmin):
    model             = SubjectInstance
    list_display      = ('subject', 'semester', 'instance_code', 'time', 'days', 'teacher', 'get_student_count')
    filter_horizontal = ('students', )
    list_filter       = ('semester', 'time', 'days', 'date_start', 'date_end', 'room')
    search_fields     = ('subject__name',  )


admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectInstance, SubjectInstanceAdmin)
