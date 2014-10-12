from django.contrib import admin
from subject_manager.models import Subject, SubjectInstance

class SubjectAdmin(admin.ModelAdmin):
    model         = Subject
    list_display  = ('code', 'name', 'units', )
    list_filter   = ('units', )
    search_fields = ('code', 'name', 'descriptions', 'room', )


class SubjectInstanceAdmin(admin.ModelAdmin):
    model             = SubjectInstance
    list_display      = ('subject', 'school_year', 'instance_code', 'time', 'days', 'get_student_count')
    filter_horizontal = ('students', )
    list_filter       = ('school_year', 'time', 'days', 'date_start', 'date_end', 'room')
    search_fields     = ('instance_code', 'time', 'days', 'room')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectInstance, SubjectInstanceAdmin)
