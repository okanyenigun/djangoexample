from django.urls import path
from cachex.views import cache_example

urlpatterns = [
    path('cache/', cache_example, name="cache"),
]