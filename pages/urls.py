from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact-us/', ContactView.as_view(), name='contact_us'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('donate/',  DonateView.as_view(), name ='donate'),

    #projects
    path('projects/human-rights/',  P1View.as_view(), name ='p1'),
    path('projects/rule-of-law/',  P2View.as_view(), name ='p2'),
    path('projects/advocacy/',  P3View.as_view(), name ='p3'),
    path('projects/lgbti-rights/', P4View.as_view(), name ='p4'),
    path('projects/transitional-justice/',  P5View.as_view(), name ='p5'),
    path('projects/migrant-rights/',  P6View.as_view(), name ='p6'),
    path('projects/human-traffiking/',  P7View.as_view(), name ='p7'),
    path('projects/international-advocacy/',  P8View.as_view(), name ='p8'),
    path('projects/civic-education/',  P9View.as_view(), name ='p9'),
    path('projects/civil-society-building/',  P10View.as_view(), name ='p10'),
    path('projects/community-mobilization/',  P11View.as_view(), name ='p11'),
    path('projects/local-governance/',  P12View.as_view(), name ='p12'),
    path('projects/displaced-persons/',  P13View.as_view(), name ='p13'),
    path('projects/independent-media/',  P14View.as_view(), name ='p14'),
    path('projects/sme-development/',  P15View.as_view(), name ='p15'),
    path('projects/local-economic-development/',  P16View.as_view(), name ='p16'),
    path('projects/agriculture-development/',  P17View.as_view(), name ='p17'),
    path('projects/womens-rights/',  P18View.as_view(), name ='p18'),
    path('projects/electoral-processes/',  P19View.as_view(), name ='p19'),
]