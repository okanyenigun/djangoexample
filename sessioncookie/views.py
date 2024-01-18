from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.views.decorators.cache import never_cache

@never_cache
def sessionvisit_view(request):
    n_visits = int(request.session.get('n_visits', 0)) + 1
    t = Template('<h1>Total visits: {{n_visits}}</h1>')
    c = Context({"n_visits": request.session["n_visits"]})
    request.session["n_visits"] = n_visits
    return HttpResponse(t.render(c))