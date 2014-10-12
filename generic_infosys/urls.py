from django.conf.urls import patterns, include, url
from django.contrib import admin

from student_profiling.views import IndexView


admin.site.site_header = 'PCT Information System'
admin.site.site_title  = 'PCT Information System'
admin.site.index_title = 'Dashboard'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
)
