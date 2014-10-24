from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View

from student_profiling.models import Student
from subject_manager.models import Subject, SubjectInstance
from school_year_manager.models import SchoolYear, Semester


class IndexView(View):
    template_name    = "student_profiling/index.html"
    context          = {}
    title            = "Home"
    context['title'] = title
    context['home_active'] = True

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('login_view'))
        if request.user.is_admin:
            return HttpResponseRedirect('/admin/')

        breadcrumb_pages = [
            {'title': 'Home', 'url': reverse('index_page'), 'is_active': False},
        ]
        self.context['breadcrumb_pages'] = breadcrumb_pages

        return render(request, self.template_name, self.context)


class RecordsView(View):
    template_name    = "student_profiling/records.html"
    context          = {}
    title            = "View Records"
    context['title'] = title
    context['records_active'] = True

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('login_view'))
        if request.user.is_admin:
            return HttpResponseRedirect('/admin/')

        year = kwargs.get("year", "")
        semester_number = kwargs.get("semester", "")

        year = int(year) if year.isdigit() else year
        semester_number = int(semester_number) if semester_number.isdigit() else semester_number

        instances = Semester.objects.filter(students__username=request.user.username).order_by("-school_year__start_year",
                                                                                               "-semester")

        if not year or not semester_number:
            s = instances[0]

            year = s.school_year.start_year
            semester_number = s.get_semester_number()

            return HttpResponseRedirect(reverse("records_semester_view",
                                                kwargs={"year": year,
                                                        "semester": semester_number}))

        breadcrumb_pages = [
            {'title': 'Home', 'url': reverse('index_page'), 'is_active': False},
            {'title': self.title, 'url': reverse('records_view'), 'is_active': True},
        ]
        self.context['breadcrumb_pages'] = breadcrumb_pages

        if semester_number is 1:
            semester_string = "1STSEM"
        if semester_number is 2:
            semester_string = "2NDSEM"
        if semester_number is 3:
            semester_string = "SUMMER"

        semester = Semester.objects.get(school_year__start_year=year,
                                        semester=semester_string)
        subject_instances = SubjectInstance.objects.filter(students__username=request.user.username,
                                                           semester=semester)

        total_units = 0
        for s in subject_instances:
            total_units += s.subject.units

        self.context['subject_instances'] = subject_instances
        self.context['total_units'] = total_units

        # still need to fix this here:
        self.context['first_record'] = False
        self.context['last_record'] = False
        self.context['prev_link'] = reverse("records_semester_view",
                                                kwargs={"year": year,
                                                        "semester": semester_number})
        self.context['next_link'] = reverse("records_semester_view",
                                                kwargs={"year": year,
                                                        "semester": semester_number})

        return render(request, self.template_name, self.context)


class SearchView(View):
    template_name    = "student_profiling/search.html"
    context          = {}
    title            = "Search Subjects"
    context['title'] = title
    context['search_active'] = True

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('login_view'))
        if request.user.is_admin:
            return HttpResponseRedirect('/admin/')

        breadcrumb_pages = [
            {'title': 'Home', 'url': reverse('index_page'), 'is_active': False},
            {'title': self.title, 'url': reverse('search_view'), 'is_active': True},
        ]
        self.context['breadcrumb_pages'] = breadcrumb_pages

        school_year = SchoolYear.objects.get(is_active=True).get_short_name()
        self.context['school_year'] = school_year

        subject_instances = SubjectInstance.objects.filter(semester__school_year__is_active=True)
        self.context['subject_instances'] = subject_instances

        return render(request, self.template_name, self.context)


class LoginView(View):
    template_name    = "student_profiling/login.html"
    context          = {}
    title            = "Login"
    context['title'] = title

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('index_page'))

        auth_form              = AuthenticationForm()
        self.context['form']   = auth_form
        errors                 = []
        self.context['errors'] = errors

        return render(request, self.template_name, self.context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        auth_form            = AuthenticationForm(request.POST)
        self.context['form'] = auth_form

        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(username=username, password=password)
        errors   = []

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index_page'))
            else:
                errors.append("Account is disabled.")
        else:
            errors.append("Invalid login credentials.")

        self.context['errors'] = errors

        return render(request, self.template_name, self.context, context_instance=RequestContext(request))


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index_page'))
