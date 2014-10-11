from django.contrib import admin
from section_manager.models import Section, SectionInstance


class SectionAdmin(admin.ModelAdmin):
    model = Section
    search_fields = ('name', )


class SectionInstanceAdmin(admin.ModelAdmin):
    model = SectionInstance
    filter_horizontal = ('students', )
    list_filter   = ('school_year', )
    search_fields = ('name', )


admin.site.register(Section, SectionAdmin)
admin.site.register(SectionInstance, SectionInstanceAdmin)
