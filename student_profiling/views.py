from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View

from student_profiling.models import Student
from subject_manager.models import Subject, SubjectInstance
from school_year_manager.models import SchoolYear


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

        breadcrumb_pages = [
            {'title': 'Home', 'url': reverse('index_page'), 'is_active': False},
            {'title': self.title, 'url': reverse('records_view'), 'is_active': True},
        ]
        self.context['breadcrumb_pages'] = breadcrumb_pages

        print kwargs

        subject_instances = SubjectInstance.objects.filter(students__username=request.user.username)
        total_units = 0
        for s in subject_instances:
            total_units += s.subject.units

        self.context['subject_instances'] = subject_instances
        self.context['total_units'] = total_units

        self.context['first_record'] = True
        self.context['last_record'] = True

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
    errors           = []

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('index_page'))

        auth_form              = AuthenticationForm()
        self.context['form']   = auth_form
        self.context['errors'] = self.errors

        return render(request, self.template_name, self.context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        auth_form            = AuthenticationForm(request.POST)
        self.context['form'] = auth_form

        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index_page'))
            else:
                self.errors.append("Account is disabled.")
        else:
            self.errors.append("Invalid login credentials.")

        self.context['errors'] = self.errors

        return render(request, self.template_name, self.context, context_instance=RequestContext(request))


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index_page'))
