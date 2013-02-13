from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', CategoryView.as_view()),
    url(r'(?P<slug>.*)/', PermalinkView.as_view()),
)