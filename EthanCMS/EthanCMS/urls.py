from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

from django.contrib import admin
admin.autodiscover()
from pages.views import MainHandler

urlpatterns = patterns('',
    # url(r'^$', 'EthanCMS.views.home', name='home'),
    # url(r'^EthanCMS/', include('EthanCMS.foo.urls')),
    url(r'^$', redirect_to, {'url': '/main/'}),

    url(r'^admin/?', include(admin.site.urls)),
    url(r'^login/?', 'EthanCMS.views.login_user'),
    url(r'^logout/?', 'EthanCMS.views.logout_user'),

    url(r'^content/', include('content.urls'), {'view_site': True}),


    # This line must be last, it handles all remaining urls
    # and will 404 if not found.
    url(r'.*', MainHandler.as_view(), {'edit_page': True}),

    # do the following to change class attributes in the urlconf
    # url(r'.*', MainHandler.as_view(class_attr='something')),
)
