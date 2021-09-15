from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact-us/', ContactView.as_view(), name='contact_us'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('donate/',  DonateView.as_view(), name ='donate'),
]