from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hip-hop', views.hip_hop),
    path('alternative-rock', views.alt_rock),
    path('auto-radio', views.auto_radio),
    path('club-dance', views.club_dance),
    path('deep-house', views.deep_house),
    path('myjam', views.myjam)
]
