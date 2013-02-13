from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from content.views import MainContentView, EditView, AddView

gallery_urls = patterns('content.gallery_views',
    url(r'^$', 'main'),
    url(r'select/', 'selector'),
    url(r'upload/', 'upload_file'),
)

urlpatterns = patterns('',
    url(r'^$', MainContentView.as_view()),
    url(r'^add/?', AddView.as_view()),
    # url(r'^add/', 'content.views.test'),
    url(r'^edit/page:(?P<url>.*)$', EditView.as_view(), {'view_page': True}),
    # url(r'^gallery/?', include(gallery_urls)),
)
