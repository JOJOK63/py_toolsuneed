from django.db import models
from django.contrib.auth.models import User

# Les choix possibles pour la devise
CURRENCY_CHOICES = [
    ("EUR", "Euro"),
    ("USD", "Dollar"),
]

# Les choix possibles pour le type de transaction
TRANSACTION_TYPE = [
    ("EXP", "Expense"),  # ⚠️ Corrigé : "TRANSFER" a 8 lettres, ton max_length=4 était trop court
    ("INC", "Income"),
    ("TRSF", "Transfer"),
]


class Category(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, unique=True)
    icon = models.ImageField(upload_to="categories/icons/", blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="subcategories/icons/", blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # catégorie obligatoire ✅

    def __str__(self) -> str:
        return self.name

class Budget(models.Model):
    name = models.CharField(max_length=255)
    detail = models.TextField(blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name




class FinancialTransaction(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    detail = models.TextField(blank=True)
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True)  # nullable ✅

    class Meta:
        db_table = "budget_financial_transaction"

    def __str__(self) -> str:
        return self.name
