from django.contrib import admin
from school_year_manager.models import SchoolYear

class SchoolYearAdmin(admin.ModelAdmin):
    model = SchoolYear
    ordering = ('start_year', )

admin.site.register(SchoolYear, SchoolYearAdmin)
