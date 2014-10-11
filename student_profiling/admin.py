from django.contrib import admin
from student_profiling.models import Student

class StudentAdmin(admin.ModelAdmin):
    model         = Student
    ordering      = ('last_name', 'first_name', )
    list_display  = ('username', 'last_name', 'first_name', 'middle_name', 'sex', 'is_active', 'is_staff', )
    list_filter   = ('sex', 'birth_date', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('last_name', 'first_name', 'middle_name',)

admin.site.register(Student, StudentAdmin)
