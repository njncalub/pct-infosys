from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    template_name = "student_profiling/index.html"
    context = {}
    title = "Home"
    context['title'] = title

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
