from django.conf.urls import patterns, include, url
from django.contrib import admin
from app1.views import homepage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hack_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homepage),
    
)
