from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from typing import Any

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "budget/index.html", context={
        "nom": request.user,
        "prenom": "John",
    })
