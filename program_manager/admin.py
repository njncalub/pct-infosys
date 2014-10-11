from django.contrib import admin
from program_manager.models import DegreeProgram

class DegreeProgramAdmin(admin.ModelAdmin):
    model = DegreeProgram
    search_fields = ('short_name', 'full_name', )

admin.site.register(DegreeProgram, DegreeProgramAdmin)
