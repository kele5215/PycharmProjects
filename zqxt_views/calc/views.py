from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from django.urls import resolvers


def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)

    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)

    return HttpResponse(str(c))


def index(request):
    return render(request, 'home.html')


def old_add2_redirect(request, a, b):
    return HttpResponsePermanentRedirect(resolvers('add2', args=(a, b)))

