import random
from typing import Any
from django.core.management.base import BaseCommand
from budget.models import Budget, Subcategory, FinancialTransaction


class Command(BaseCommand):
    help = "Crée des transactions de test."

    def handle(self, *args: Any, **options: Any) -> None:
        budgets = list(Budget.objects.all())
        subcategories = list(Subcategory.objects.all())

        if not budgets or not subcategories:
            self.stdout.write(self.style.ERROR("Lance d'abord seed_budgets et seed_categories."))
            return

        types = ["EXP", "INC", "TRSF"]
        names = ["Courses", "Salaire", "Restaurant", "Essence", "Loyer", "Cinéma"]

        for i in range(20):
            FinancialTransaction.objects.create(
                name=random.choice(names),
                amount=round(random.uniform(5, 500), 2),
                detail=f"Transaction test #{i}",
                transaction_type=random.choice(types),
                budget=random.choice(budgets),
                subcategory=random.choice(subcategories),
            )

        self.stdout.write(self.style.SUCCESS("20 transactions créées !"))