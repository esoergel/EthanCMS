from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect
import json
from django.views.generic import View, DetailView, TemplateView, ListView
from pages.models import Page
from EthanCMS.config import ContentMixin
from dev import Dev


class MainHandler(Dev, ContentMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        self.page = self.get_page_from_path(request.path)
        context['page'] = self.page
        self.template_name = self.page.template
        return self.render_to_response(context)

    def get_page_from_path(self, path):
        if path[-1] != '/':
            path += '/'
        return get_object_or_404(Page, url=path)

