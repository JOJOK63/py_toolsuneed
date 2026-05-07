from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Category, Subcategory
from .serializers import CategorySerializer, SubcategorySerializer


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "budget/index.html", context={
        "nom": request.user,
        "prenom": "John",
    })


# API //////////////////////
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class SubcategoryListCreateView(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

class SubcategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    lookup_field = 'id'