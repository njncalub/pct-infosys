from django.contrib import admin
from program_manager.models import DegreeProgram

class DegreeProgramAdmin(admin.ModelAdmin):
    model = DegreeProgram
    list_display = ('short_name', 'full_name', )
    search_fields = ('short_name', 'full_name', )

admin.site.register(DegreeProgram, DegreeProgramAdmin)
