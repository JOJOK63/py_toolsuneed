from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model  # <-- On utilise le sélecteur dynamique
from budget.models import Budget

# Récupère le bon modèle User (auth_app.User) configuré dans ton projet
User = get_user_model()


class Command(BaseCommand):
    help = "Crée des budgets de test liés à des utilisateurs."

    def handle(self, *args: Any, **options: Any) -> None:
        try:
            admin = User.objects.get(username='admin')
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Lance d'abord seed_users."))
            return

        budgets_data = [
            {"name": "Budget principal", "detail": "Compte courant", "balance": 1500.00, "currency": "EUR"},
            {"name": "Épargne", "detail": "Livret A", "balance": 5000.00, "currency": "EUR"},
        ]

        for data in budgets_data:
            budget, created = Budget.objects.update_or_create(
                name=data["name"],
                user=admin,
                defaults=data
            )
            if created:
                self.stdout.write(f"Budget créé : '{data['name']}'")

        self.stdout.write(self.style.SUCCESS("Peuplement des budgets terminé !"))