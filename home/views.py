from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """View for homepage
    """

    template_name = "home/index.html"
