from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Page HTML
    path('', views.index, name="budget-index"),

    # API
    path('category/', views.CategoryListCreateView.as_view()),
    path('category/<int:id>/', views.CategoryRetrieveUpdateDestroyView.as_view()),

    path('subcategory/', views.SubcategoryListCreateView.as_view()),
    path('subcategory/<int:id>/', views.SubcategoryRetrieveUpdateDestroyView.as_view()),
]
