from django.contrib import admin

from teacher_profiling.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    model         = Teacher
    list_display  = ('get_full_name', 'last_name', 'first_name', 'middle_name', 'sex', 'birth_date', )
    list_filter   = ('sex', 'birth_date', )
    search_fields = ('last_name', 'first_name', 'middle_name', )

admin.site.register(Teacher, TeacherAdmin)
