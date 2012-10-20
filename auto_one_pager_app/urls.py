# Create a means to interpret the various urls 

from django.conf.urls import patterns, url

# get the views as defined in root folder for the app
from auto_one_pager_app import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index')
)