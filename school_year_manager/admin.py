from django.contrib import admin
from school_year_manager.models import SchoolYear, Semester


class SchoolYearAdmin(admin.ModelAdmin):
    model         = SchoolYear
    ordering      = ('start_year', )
    list_display  = ('__unicode__', 'start_year', 'end_year', 'is_active', )
    list_filter   = ('is_active', )
    search_fields = ('start_year', 'end_year', )


class SemesterAdmin(admin.ModelAdmin):
    model             = Semester
    ordering          = ('school_year', )
    list_display      = ('__unicode__', 'semester', 'school_year', 'get_student_count', )
    list_filter       = ('semester', 'school_year__start_year', )
    search_fields     = ('semester', )
    filter_horizontal = ('students', )


admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(Semester, SemesterAdmin)
