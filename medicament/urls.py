from django.conf.urls import patterns, include, url
from django.contrib import admin
from medicament import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Medic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.monitor_type_list),
    url(r'^form1$', views.monitoring_list),
    url(r'^monitor/$', views.monitoring_form),
    url(r'^monitor/(?P<question_id>\d+)/$', views.monitoring_form, name='monitoring_form'),
    url(r'^monitor/add_comment/(?P<question_id>\d+)/$', views.add_comment, name='add_comment'),
    

)
