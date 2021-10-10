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
    
class P1View(TemplateView):
    template_name = "projects/p1.html"

class P2View(TemplateView):
    template_name = "projects/p2.html"

class P3View(TemplateView):
    template_name = "projects/p3.html"

class P4View(TemplateView):
    template_name = "projects/p4.html"

class P5View(TemplateView):
    template_name = "projects/p5.html"

class P6View(TemplateView):
    template_name = "projects/p6.html"

class P7View(TemplateView):
    template_name = "projects/p7.html"

class P8View(TemplateView):
    template_name = "projects/p8.html"

class P9View(TemplateView):
    template_name = "projects/p9.html"

class P10View(TemplateView):
    template_name = "projects/p10.html"

class P11View(TemplateView):
    template_name = "projects/p11.html"

class P12View(TemplateView):
    template_name = "projects/p12.html"

class P13View(TemplateView):
    template_name = "projects/p13.html"

class P14View(TemplateView):
    template_name = "projects/p14.html"

class P15View(TemplateView):
    template_name = "projects/p15.html"

class P16View(TemplateView):
    template_name = "projects/p16.html"

class P17View(TemplateView):
    template_name = "projects/p17.html"

