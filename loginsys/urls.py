from django.conf.urls import patterns, include, url
from django.contrib import admin
from loginsys.views import login,logout,registeruser

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PhotoAlbum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
  
    url(r'^login/', login, name = 'login'),
    url(r'^logout/',logout, name = 'logout'),
 #   url(r'^register/',registeruser, name = 'registeruser')
       
)
