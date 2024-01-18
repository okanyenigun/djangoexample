from django.urls import path
from .views import sessionvisit_view

urlpatterns = [
    path('sessioncookie/', sessionvisit_view),
]
