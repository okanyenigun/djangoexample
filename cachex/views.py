import time
from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponse
from cachex.models import DummyModel

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

