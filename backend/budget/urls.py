from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Page HTML
    path('', views.index, name="budget-index"),

    # API
    # Category
    path('category/', views.CategoryListCreateView.as_view()),
    path('category/<int:id>/', views.CategoryRetrieveUpdateDestroyView.as_view()),

    # Subcategory
    path('subcategory/', views.SubcategoryListCreateView.as_view()),
    path('subcategory/<int:id>/', views.SubcategoryRetrieveUpdateDestroyView.as_view()),

    # Budget
    path('budget/', views.BudgetListCreateView.as_view()),
    path('budget/<int:id>/', views.BudgetRetrieveUpdateDestroyView.as_view()),

    # Financial Transactions
    path('financial-transaction/', views.FinancialTransactionListCreateView.as_view()),
    path('financial-transaction/<int:id>/', views.FinancialTransactionRetrieveUpdateDestroyView.as_view()),

]
