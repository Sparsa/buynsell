from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('C2C.views',  # This is the patterns which get attached with the urls to give
                       #  location of the files.
    # Examples:
    # url(r'^$', 'buynsell.views.home', name='home'),
    # url(r'^buynsell/', include('buynsell.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$','index'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg/$', 'registration'),

    url(r'^oops/$', 'oops'),
    url(r'^search/$', 'search'),
    url(r'^loginf/$', TemplateView.as_view(template_name="login_form.html")),
    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),
    url(r'^advertisement/$', 'add'),
)
