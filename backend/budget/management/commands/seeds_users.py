from typing import Any
from django.core.management.base import BaseCommand
from auth_app.models import User  # Correction subtile de l'import au passage (django.contrib.auth_app n'existe pas)


class Command(BaseCommand):
    help = "Crée des utilisateurs de test."

    def handle(self, *args: Any, **options: Any) -> None:
        # On ajoute le typage ici :
        users_data: list[dict[str, Any]] = [
            {"username": "admin", "email": "admin@test.com", "is_superuser": True, "is_staff": True},
            {"username": "alice", "email": "alice@test.com"},
            {"username": "bob", "email": "bob@test.com"},
        ]

        for data in users_data:
            username = data.pop("username")
            user, created = User.objects.get_or_create(
                username=username,
                defaults=data  # Note : pas besoin de faire {**data}, vous pouvez passer directement 'data'
            )
            if created:
                user.set_password("testpass123")
                user.save()
                self.stdout.write(f"Utilisateur créé : '{username}'")
            else:
                self.stdout.write(f"Utilisateur existant : '{username}'")

        self.stdout.write(self.style.SUCCESS("Peuplement des utilisateurs terminé !"))