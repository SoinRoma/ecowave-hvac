from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class BlogDetailView(TemplateView):
    template_name = 'detail.html'


class ServiceView(TemplateView):
    template_name = 'service.html'


class AboutView(TemplateView):
    template_name = 'about.html'
