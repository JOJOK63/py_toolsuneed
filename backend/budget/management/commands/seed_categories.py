from typing import Any
from django.core.management.base import BaseCommand
from budget.models import Category, Subcategory

class Command(BaseCommand):
    help = "Peuple la base de données avec les catégories et sous-catégories initiales."

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write("Début du peuplement des catégories...")

        CATEGORIES_DATA = {
            "Achats & shopping": {
                "color": "#FF5722",  # Orange Foncé
                "icon": "shopping-cart",
                "subcategories": [
                    "articles de sport", "cadeaux", "dons",
                    "high tech, jeux vidéos", "vêtements, chaussures, accessoires", "autres"
                ]
            },
            "Alimentation": {
                "color": "#4CAF50",  # Vert
                "icon": "utensils",
                "subcategories": [
                    "Marché", "Restaurants, snacks", "Supermarché, épicerie", "Alcool", "Alimentation autres"
                ]
            },
            "Animaux": {
                "color": "#FF9800",  # Ambre / Orange clair
                "icon": "paw",
                "subcategories": [
                    "jouets", "mutuelle", "nourriture", "Santé, soins", "Animaux autres"
                ]
            },
            "Assurances & prévoyance": {
                "color": "#9C27B0",  # Violet
                "icon": "shield-alt",
                "subcategories": []
            },
            "Crédits": {
                "color": "#E91E63",  # Rose / Magenta
                "icon": "hand-holding-usd",
                "subcategories": []
            },
            "Enfants": {
                "color": "#00BCD4",  # Cyan
                "icon": "child",
                "subcategories": [
                    "Activités enfants", "Argent de poche", "Assurances enfants",
                    "Fourniture scolaire", "Frais de scolarité", "Garde d'enfants",
                    "Jouets, cadeaux", "Pensions alimentaires", "Enfants autres"
                ]
            },
            "Epargne et placements": {
                "color": "#009688",  # Turquoise / Teal
                "icon": "piggy-bank",
                "subcategories": []
            },
            "Impots taxe et frais": {
                "color": "#607D8B",  # Bleu Gris (Slate)
                "icon": "file-invoice-dollar",
                "subcategories": [
                    "Amendes", "Contributions sociales", "Frais bancaires",
                    "Impôts sur la fortune", "Impôts sur le revenu",
                    "Taxes foncières, d'habitation", "Impots, taxe & frais autres"
                ]
            },
            "Logements et charge": {
                "color": "#2196F3",  # Bleu standard
                "icon": "home",
                "subcategories": [
                    "Assurance logement", "Charges logement et accessoires",
                    "Eau, électricité, gaz", "Internet, téléphonie", "Loyer",
                    "Prêt immobilier", "Résidence secondaire", "Travaux entretien", "Logement & charges autres"
                ]
            },
            "Loisirs et vacance": {
                "color": "#9E9E9E",  # Gris
                "icon": "umbrella-beach",
                "subcategories": [
                    "Abonnement multimédia", "Bars & clubs", "Coiffeur, esthétique",
                    "Sorties culturelles", "Sport", "Vacances, voyages", "Loisirs & vacances autres"
                ]
            },
            "Retraits": {
                "color": "#795548",  # Marron
                "icon": "money-bill-wave",
                "subcategories": []
            },
            "Santé": {
                "color": "#F44336",  # Rouge
                "icon": "heartbeat",
                "subcategories": [
                    "Médecin", "Mutuelle", "Optique", "Pharmacie", "Santé - autres"
                ]
            },
            "Transport": {
                "color": "#3F51B5",  # Indigo / Bleu nuit
                "icon": "car",
                "subcategories": [
                    "assurance véhicule", "avion, train bateau", "carburant",
                    "Entretien, équipement véhicule", "Location véhicule", "péage",
                    "prêt véhicule", "Stationnement", "Taxi, VTC", "Transport en commun", "Transport autres"
                ]
            },
            "Travail & études": {
                "color": "#673AB7",  # Violet foncé / Deep Purple
                "icon": "graduation-cap",
                "subcategories": [
                    "Dépenses professionnelles", "Notes de frais", "Prêt étudiant",
                    "Repas au travail", "Travail & études - autres"
                ]
            }
        }

        for cat_name, cat_info in CATEGORIES_DATA.items():
            category, created = Category.objects.update_or_create(
                name=cat_name,
                defaults={
                    "color": cat_info["color"],
                    "icon": cat_info["icon"],
                    "is_active": True
                }
            )

            if created:
                self.stdout.write(f"Catégorie créée : '{cat_name}'")
            else:
                self.stdout.write(f"Catégorie existante mise à jour : '{cat_name}'")

            for sub_name in cat_info["subcategories"]:
                subcategory, sub_created = Subcategory.objects.update_or_create(
                    name=sub_name,
                    category=category
                )
                if sub_created:
                    self.stdout.write(f"   -> Sous-catégorie créée : '{sub_name}'")

        self.stdout.write(self.style.SUCCESS("Peuplement terminé avec succès !"))