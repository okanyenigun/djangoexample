from django.urls import path
from cachex.views import cache_example,redis_view

urlpatterns = [
    path('cache/', cache_example, name="cache"),
    path('cacheRedis/', redis_view, name="cache_redis"),
]