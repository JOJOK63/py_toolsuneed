from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'todolist/index.html', context={})


def add_collection(request: HttpRequest) -> HttpResponse:
    return render(request, 'todolist/add-collection.html', context={})


def add_todo(request: HttpRequest) -> HttpResponse:
    return HttpResponse("")
