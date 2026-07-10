# 1. Charger le fichier .env s'il existe
ifneq (,$(wildcard .env))
    include .env
    export
endif

# --- Variables de Configuration ---
DOCKER_COMPOSE=docker-compose.yaml
BACKEND_SERVICE=backend
FRONTEND_SERVICE=frontend
DB_SERVICE=db

# Déclaration des cibles feintes (évite les conflits avec des fichiers/dossiers du même nom)
.PHONY: build up down restart status logs logs-b logs-f logs-db \
        mm migrate migration flush seed reset-db db-su cu \
        ct-b ct-f ct-db clean-v

# ==============================================================================
# 🚀 LANCEMENT, ARRÊT & STATUT
# ==============================================================================

build:
	docker compose -f $(DOCKER_COMPOSE) build

up:
	docker compose -f $(DOCKER_COMPOSE) up -d

down:
	docker compose -f $(DOCKER_COMPOSE) down

restart: down up

status:
	docker compose -f $(DOCKER_COMPOSE) ps

# ==============================================================================
# 🗄️ BASE DE DONNÉES & MIGRATIONS (DJANGO)
# ==============================================================================

# Étape 1 : Générer les fichiers de migration basés sur vos modèles Python
mm:
	docker compose exec $(BACKEND_SERVICE) python manage.py makemigrations

# Étape 2 : Appliquer les fichiers de migration en base de données Postgres
mig:
	docker compose exec $(BACKEND_SERVICE) python manage.py migrate

# Le Combo : Génère ET applique la migration en une seule commande
migration: mm migrate

# Vide TOUTES les tables de la DB (sans supprimer les tables elles-mêmes)
flush:
	docker compose exec $(BACKEND_SERVICE) python manage.py flush --no-input

# Remplit la DB avec vos données de test (Command maîtresse)
seed:
	docker compose exec $(BACKEND_SERVICE) python manage.py seed_all

# Le Reset Ultime : Vide tout, réapplique l'historique et repeuple à neuf
reset-db: flush migrate seed
	@echo "============================================="
	@echo " 🔥 Base de données réinitialisée et re-peuplée ! 🔥 "
	@echo "============================================="

# ==============================================================================
# 👤 GESTION DES UTILISATEURS (DJANGO)
# ==============================================================================

# Création interactive d'un superutilisateur
db-su:
	docker compose exec $(BACKEND_SERVICE) python manage.py createsuperuser

# Création automatique du superutilisateur via les variables du .env
cu:
	docker compose exec $(BACKEND_SERVICE) python manage.py createsuperuser --noinput || true

# Configuration initiale complète du projet
setup: build up
	@echo "En attente du démarrage complet et des migrations automatiques..."
	@sleep 5
	docker compose exec $(BACKEND_SERVICE) python manage.py createsuperuser --noinput || true
	@echo "============================================="
	@echo "🚀 Application prête !"
	@echo "Admin créé avec les identifiants du fichier .env"
	@echo "============================================="

# ==============================================================================
# 🖥️ ACCÈS DIRECT AUX CONTENEURS (SHELL)
# ==============================================================================

ct-b:
	docker compose exec $(BACKEND_SERVICE) bash

ct-f:
	docker compose exec $(FRONTEND_SERVICE) bash

ct-db:
	docker compose exec $(DB_SERVICE) psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

# ==============================================================================
# 📋 LOGS & NETTOYAGE
# ==============================================================================

logs:
	docker compose -f $(DOCKER_COMPOSE) logs -f

logs-b:
	docker compose -f $(DOCKER_COMPOSE) logs $(BACKEND_SERVICE)

logs-f:
	docker compose -f $(DOCKER_COMPOSE) logs $(FRONTEND_SERVICE)

logs-db:
	docker compose -f $(DOCKER_COMPOSE) logs $(DB_SERVICE)

clean-v:
	docker compose -f $(DOCKER_COMPOSE) down -v