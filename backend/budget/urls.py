from django.urls import path

from .views import index, budget

urlpatterns = [
    path('',index, name="budget-index"),
    path('budget-<str:number_budget>/',budget, name="budget-detail")
]
