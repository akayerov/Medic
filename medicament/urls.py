from django.conf.urls import patterns, include, url
from django.contrib import admin
from medicament import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Medic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.monitor_type_list),
    url(r'^form1$', views.monitoring_list),
    

)
