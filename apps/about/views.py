from django.shortcuts import render
from django.views import View, generic

from .models import AboutUs

class AboutView(generic.ListView):
    model = AboutUs
    template_name = 'about/about.html'
    context_object_name = 'abouts'