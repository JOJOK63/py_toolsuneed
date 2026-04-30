from django.urls import path
from .views import index, add_collection

urlpatterns = [
    path('', index, name="todolist-index"),
    path('add-collection', add_collection, name="add-collection"),
]
