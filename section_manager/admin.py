from django.contrib import admin
from section_manager.models import Section, SectionInstance


class SectionAdmin(admin.ModelAdmin):
    model         = Section
    list_display  = ('name', 'degree_program', 'year_level', )
    list_filter   = ('year_level', 'degree_program', )
    search_fields = ('name', )


class SectionInstanceAdmin(admin.ModelAdmin):
    model             = SectionInstance
    list_display      = ('section', 'get_year_level', 'get_degree_program', 'get_school_year', 'get_student_count', )
    list_filter       = ('school_year__start_year', 'section__year_level', 'section__degree_program', )
    search_fields     = ('section__name', )
    filter_horizontal = ('students', )


admin.site.register(Section, SectionAdmin)
admin.site.register(SectionInstance, SectionInstanceAdmin)
