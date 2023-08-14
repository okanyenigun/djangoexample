import time
from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from cachex.models import DummyModel
from cachex.business import fibonacci

def create_records():
    # Generate 1000 dummy records using Faker
    for _ in range(1000):
        DummyModel.objects.create()
    return HttpResponse('Records created successfully')

def delete_records():
    # Delete all records from the DummyModel
    DummyModel.objects.all().delete()
    cache.clear()
    return HttpResponse('All records deleted successfully')

def cache_example(request):
    data = {}
    context = {}
    start_time = time.time()
    if "cache" in request.GET:
        # use cache
        data = cache.get('dummy_data')
        if not data:
            # if there is no data in the cache first pull and then store them in cache
            data = list(DummyModel.objects.all().values())
            cache.set('dummy_data', data, 60)
    if "db" in request.GET:
        # get from database
        data = list(DummyModel.objects.all().values())
    if "create" in request.GET:
        create_records()
    if "del" in request.GET:
        delete_records()
    end_time = time.time()
    context["time"] = end_time - start_time
    context["length"] = len(data)
    return render(request, './templates/cache.html', context)


    
# View function without caching
# def redis_view(request):
#     n=35
#     start_time = time.time()
#     result = fibonacci(n)
#     end_time = time.time()
#     duration = end_time - start_time
#     return render(request, './templates/cache_redis.html', {'n': n, 'result': result, 'duration': duration})

# View function with caching page cache
# @cache_page(60 * 5) 
# def redis_view(request):
#     n=35
#     start_time = time.time()
#     result = fibonacci(n)
#     end_time = time.time()
#     duration = end_time - start_time
#     return render(request, './templates/cache_redis.html', {'n': n, 'result': result, 'duration': duration})

# view function with low level
# def redis_view(request):
#     n = 35
#     start_time = time.time()
#     result = cache.get('fibonacci')
#     if result is None:
#         result = fibonacci(n)
#         cache.set('fibonacci', result, 30)
#     end_time = time.time()
#     duration = end_time - start_time
#     return render(request, './templates/cache_redis.html', {'n': n, 'result': result, 'duration': duration})

# view function for database cache
# def redis_view(request):
#     n = 35
#     start_time = time.time()
#     result = cache.get('fibonacci')
#     if result is None:
#         result = fibonacci(n)
#         cache.set('fibonacci', result, 30)
#     end_time = time.time()
#     duration = end_time - start_time
#     return render(request, './templates/cache_redis.html', {'n': n, 'result': result, 'duration': duration})


# def filesystem_cache_view(request):
#     n = 35
#     start_time = time.time()
#     data = cache.get('mykey')
#     if data is None:
#         data = fibonacci(n)
#         cache.set('mykey', data, 60 * 15)
#     end_time = time.time()
#     duration = end_time - start_time
#     return render(request, './templates/cache_redis.html', {'n': n, 'result': data, 'duration': duration})
    
def local_memory_cache_view(request):
    n = 35
    data = cache.get('mykey')
    if data is None:
        data = fibonacci(n)
        cache.set('mykey', data, 60 * 15)
    return render(request, './templates/cache_redis.html', {'n': n, 'result': data})