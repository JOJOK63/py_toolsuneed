from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.serializers import BaseSerializer
from .models import Category, Subcategory, Budget, FinancialTransaction
from .serializers import (
    CategorySerializer,
    SubcategorySerializer,
    BudgetSerializer,
    FinancialTransactionSerializer,
)


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "budget/index.html", context={
        "nom": request.user,
        "prenom": "John",
    })


# CATEGORY ////////////////
@extend_schema(tags=["Budget / Category"])
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema(tags=["Budget / Category"])
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    lookup_field = 'id'


# SUBCATEGORY //////////////
@extend_schema(tags=["Budget / Subcategory"])
@extend_schema(
    tags=["Budget / Subcategory"],
    parameters=[
        OpenApiParameter(
            name='category',
            type=int,
            description='Filtre par catégorie (id)',
        )
    ]
)
class SubcategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = SubcategorySerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_queryset(self) -> QuerySet:
        category_id = self.request.query_params.get('category')
        if category_id:
            return Subcategory.objects.filter(category_id=category_id)
        return Subcategory.objects.all()


@extend_schema(tags=["Budget / Subcategory"])
class SubcategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    lookup_field = 'id'


# BUDGET //////////////////
@extend_schema(
    tags=["Budget / Budget"]
)
class BudgetListCreateView(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer

    def get_queryset(self) -> QuerySet:
        # TODO → self.request.user quand auth en place
        # Pour l'instant AnonymousUser → retourne tout
        user = self.request.user
        if user.is_authenticated:
            return Budget.objects.filter(user=user)
        return Budget.objects.all()

    def perform_create(self, serializer: BaseSerializer) -> None:
        # Injecte le user connecté à la création
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            # Temporaire — admin par défaut sans auth
            default_user = User.objects.get(username='admin')
            serializer.save(user=default_user)


@extend_schema(tags=["Budget / Budget"])
class BudgetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_field = 'id'


# FINANCIAL TRANSACTION ///
# @extend_schema use to groupe by model on swagger api
# OpenApiParameter use to understand what param endpoint need because swagger d'ont reed python
@extend_schema(
    tags=["Budget / Financial Transaction"],
    parameters=[
        OpenApiParameter(
            name='budget',
            type=int,
            description='Filtre par budget (id) — obligatoire',
            required=True,
        )
    ]
)
class FinancialTransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = FinancialTransactionSerializer

    def get_queryset(self) -> QuerySet:
        budget_id = self.request.query_params.get('budget')
        if not budget_id:
            return FinancialTransaction.objects.none()
        return FinancialTransaction.objects.filter(budget_id=budget_id)


@extend_schema(tags=["Budget / Financial Transaction"])
class FinancialTransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FinancialTransaction.objects.all()
    serializer_class = FinancialTransactionSerializer
    lookup_field = 'id'
