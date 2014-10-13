from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from student_profiling.models import Student


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Student
        # fields = ('email', 'birth_date', )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Student
        fields = ('email',
                  'password',
                  'birth_date',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'sex',
                  'birth_date',
                  'degree_program',
                  'address',
                  'mobile_number',
                  'landline_number',
                  'website_address',
                  'is_active',
                  'is_staff',
                  'is_admin',
                 )

    def clean_password(self):
        return self.initial["password"]


class StudentAdmin(UserAdmin):
    form         = UserChangeForm
    add_form     = UserCreationForm

    list_display = ('username', 'last_name', 'first_name', 'middle_name', 'sex', 'is_active', 'is_staff', )
    list_filter  = ('sex', 'birth_date', 'is_active', 'is_staff', 'is_superuser', )

    fieldsets = (
        (None,
            {'fields': ('username',
                        'email',
                        'password',
            )}),
        ('Personal info',
            {'fields': ('birth_date',
                        'last_name',
                        'first_name',
                        'middle_name',
                        'sex',
                        'degree_program',
                        'address',
                        'mobile_number',
                        'landline_number',
                        'website_address',
            )}),
        ('Permissions',
            {'fields': ('is_active',
                        'is_staff',
                        'is_admin',
            )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username',
                       'email',
                       'password1',
                       'password2',
                       'last_name',
                       'first_name',
                       'middle_name',
                       'sex',
                       'birth_date',
                       'degree_program',
                       'address',
                       'mobile_number',
                       'landline_number',
                       'website_address',
                       'is_active',
                       'is_staff',
                       'is_admin',
            )}
        ),
    )
    search_fields = ('last_name', 'first_name', 'middle_name', )
    ordering = ('last_name', 'first_name', )
    filter_horizontal = ()


admin.site.register(Student, StudentAdmin)
admin.site.unregister(Group)




# class StudentAdmin(UserAdmin):
#     model         = Student
#     ordering      = ('last_name', 'first_name', )
#     list_display  = ('username', 'last_name', 'first_name', 'middle_name', 'sex', 'is_active', 'is_staff', )
#     list_filter   = ('sex', 'birth_date', 'is_active', 'is_staff', 'is_superuser', )
#     search_fields = ('last_name', 'first_name', 'middle_name', )

# admin.site.register(Student, StudentAdmin)
