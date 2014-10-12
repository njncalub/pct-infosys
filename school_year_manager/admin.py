from django.contrib import admin
from school_year_manager.models import SchoolYear

class SchoolYearAdmin(admin.ModelAdmin):
    model         = SchoolYear
    ordering      = ('start_year', )
    list_display  = ('__unicode__', 'start_year', 'end_year', 'is_active', )
    list_filter   = ('is_active', )
    search_fields = ('start_year', 'end_year', )

admin.site.register(SchoolYear, SchoolYearAdmin)
