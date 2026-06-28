# 1. Charger le fichier .env s'il existe
ifneq (,$(wildcard .env))
    include .env
    export
endif

# Variables de services
DOCKER_COMPOSE=docker-compose.yaml
BACKEND_SERVICE=backend
FRONTEND_SERVICE=frontend
DB_SERVICE=db

.PHONY: up down build logs migrate seed setup restart status clean-v backc frontc dbc

# --- Lancement et Arrêt ---

build:
	docker compose -f $(DOCKER_COMPOSE) build
	
up:
	docker compose -f $(DOCKER_COMPOSE) up -d

down:
	docker compose -f $(DOCKER_COMPOSE) down


# --- Maintenance & Base de données ---
migrate:
	docker compose exec $(BACKEND_SERVICE) python manage.py migrate

seed:
	docker compose exec $(BACKEND_SERVICE) python manage.py seed_categories

# --- Accès direct aux Conteneurs ---
ct-b:
	docker compose exec $(BACKEND_SERVICE) bash

ct-f:
	docker compose exec $(FRONTEND_SERVICE) bash

# REGARDEZ ICI : On utilise les variables $(POSTGRES_USER) et $(POSTGRES_DB) lues depuis le .env !
ct-db:
	docker compose exec $(DB_SERVICE) psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

# création du super user
db-su:
	docker compose exec $(BACKEND_SERVICE) python manage.py createsuperuser

# --- Commandes Groupées ---
setup: build up
	@echo "En attente du démarrage complet et des migrations automatiques..."
	@sleep 5 # On laisse quelques secondes à Django pour finir ses migrations internes
	docker compose exec $(BACKEND_SERVICE) python manage.py createsuperuser --noinput || true
	@echo "============================================="
	@echo "Application prête !"
	@echo "Admin créé avec les identifiants du fichier .env"
	@echo "============================================="

# ----- Migration -----

mm:
	docker compose exec $(BACKEND_SERVICE) python manage.py makemigrations

##### Logs généraux ou pour chaque container
logs:
	docker compose -f $(DOCKER_COMPOSE) logs -f

logs-b:
	docker compose -f $(DOCKER_COMPOSE) logs $(BACKEND_SERVICE)

logs-f:
	docker compose -f $(DOCKER_COMPOSE) logs $(FRONTEND_SERVICE)

logs-db:
	docker compose -f $(DOCKER_COMPOSE) logs $(DB_SERVICE)

status:
	docker compose -f $(DOCKER_COMPOSE) ps

clean-v:
	docker compose -f $(DOCKER_COMPOSE) down -v