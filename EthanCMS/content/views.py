from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.utils import timezone
# from blog.views import permalink_handler
# from django.conf import settings

from django.views.generic import ListView, UpdateView, CreateView
from dev import Dev
from pages.models import Page, Tag
from EthanCMS.config import ContentMixin, DEFAULT_TEMPLATE


class PageFormMixin(object):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form, **kwargs))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_invalid(self, form, **kwargs):
        return self.render_to_response(self.get_context_data(form=form, **kwargs))

    def form_valid(self, form, **kwargs):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class MainContentView(ContentMixin, ListView):
    model = Page
    template_name = "content/main.html"
    # context_object_name = 'page'


class EditView(PageFormMixin, ContentMixin, UpdateView):
    model = Page
    template_name = "content/post-edit.html"
    slug_field = 'url'
    slug_url_kwarg = 'url'


class AddView(PageFormMixin, ContentMixin, CreateView):
    model = Page
    template_name = "content/post-edit.html"
    initial = {'template': DEFAULT_TEMPLATE}

    def get_object(self):
        return None

    def get_success_url(self):
        print self.object
        return self.object.url