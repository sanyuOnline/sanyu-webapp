from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "pages/home.html"
    
class AboutView(TemplateView):
    template_name = "pages/about.html"

class ProjectsView(TemplateView):
    template_name = "pages/projects.html"

class ContactView(TemplateView):
    template_name = "pages/contact-us.html"

class DonateView(TemplateView):
    template_name = "pages/donate.html"
