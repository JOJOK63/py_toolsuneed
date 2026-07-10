from typing import Any
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Exécute toutes les commandes de peuplement (seeds) dans le bon ordre."

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write(self.style.WARNING("Début du peuplement global de la base de données..."))

        # 1. On crée d'abord les utilisateurs (indépendants)
        self.stdout.write("Exécution de seeds_users...")
        call_command("seeds_users")

        # 2. On crée les catégories (indépendantes ou liées aux utilisateurs)
        self.stdout.write("Exécution de seed_categories...")
        call_command("seed_categories")

        # 3. On crée les budgets (dépendent des utilisateurs et des catégories)
        self.stdout.write("Exécution de seed_budgets...")
        call_command("seed_budgets")

        # 4. On crée les transactions (dépendent des budgets)
        self.stdout.write("Exécution de seed_transactions...")
        call_command("seed_transactions")

        self.stdout.write(self.style.SUCCESS("Tout a été peuplé avec succès !"))