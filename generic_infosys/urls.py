from django.conf.urls import patterns, include, url
from django.contrib import admin

from student_profiling.views import (IndexView, LoginView, LogoutView,
                                     RecordsView, SearchView, )


admin.site.site_header = 'PCT Information System'
admin.site.site_title  = 'PCT Information System'
admin.site.index_title = 'Dashboard'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', LoginView.as_view(), name="login_view"),
    url(r'^logout/$', LogoutView.as_view(), name="logout_view"),

    url(r'^records/$', RecordsView.as_view(), name="records_view"),
    url(r'^records/(?P<year>\d{4})/(?P<semester>\d{4})/$', RecordsView.as_view(), name="records_view"),
    url(r'^search/$', SearchView.as_view(), name="search_view"),

    url(r'^$', IndexView.as_view(), name="index_page"),
)
