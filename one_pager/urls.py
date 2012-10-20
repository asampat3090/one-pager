from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^auto_one_pager_app/', include('auto_one_pager_app.urls')),
                       
    # Examples:
    # url(r'^$', 'one_pager.views.home', name='home'),
    # url(r'^one_pager/', include('one_pager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # corresponding url in urls.py
    # url(r'^mark_done/(\d*)/$', 'dbe.todo.views.mark_done'),
)
