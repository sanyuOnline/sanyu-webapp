from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('dashboard/<int:pk>/', UserDashBoardView.as_view(), name='user_dash'),
]
