from django.urls import path
from .views import chess_endpoint

urlpatterns = [
    path('chess/<slug>', chess_endpoint, name='chess_endpoint'),
]
