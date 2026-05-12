from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.serializers import BaseSerializer

from .models import Category, Subcategory, Budget
from .serializers import CategorySerializer, SubcategorySerializer, BudgetSerializer


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "budget/index.html", context={
        "nom": request.user,
        "prenom": "John",
    })


# API //////////////////////

# Category ////////////////
@extend_schema(tags=["Budget / Category"])
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema(tags=["Budget / Category"])
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


# Subcategory //////////////
@extend_schema(tags=["Budget / Subcategory"])
class SubcategoryListCreateView(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema(tags=["Budget / Subcategory"])
class SubcategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    lookup_field = 'id'


# Budget /////////////
@extend_schema(tags=["Budget / Budget"])
class BudgetListCreateView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    # injection du user a étudié en détail pour comprendre, inecjtect automatiquement le user admin connecté si je ne dis pas de bétises
    # TODO voir commment ajouter l'utilisateur authentifier et non l'admin
    def perform_create(self, serializer : BaseSerializer) -> None:
        serializer.save(user=self.request.user)


@extend_schema(tags=["Budget / Budget"])
class BudgetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_field = 'id'
