🛠️ ToolsUNeed — Guide de mise en place et d'utilisation
📋 Stack technique
Composant	Technologie	Port
Base de données	PostgreSQL 16	5432
Backend	Django (Python 3.12)	8000
Frontend	Vite / Vue.js (Node 20)	5173
⚙️ Prérequis

    Docker (v20+) et Docker Compose (v2+)

    Make (installé par défaut sur Linux/Mac, disponible via Chocolatey/WSL sur Windows)


Configuration de l'environnement

Avant de lancer l'application, crée un fichier .env à la racine du projet et copies-y la configuration suivante :

# ==============================================================================
# CONFIGURATION LOCAL / DÉVELOPPEMENT (Exemple type)
# ==============================================================================

# --- CONFIGURATION POSTGRES ---
POSTGRES_DB=toolsuneed
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword

# --- CONFIGURATION ADMIN DJANGO ---
# Ces identifiants seront utilisés automatiquement lors du 'make setup'
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=mypassword

🚀 Démarrage Rapide (Première installation)

Pour construire les images, lancer les conteneurs, appliquer les migrations et initialiser le super-utilisateur d'un seul coup :
Bash

make setup

    💡 Cette commande utilise les variables DJANGO_SUPERUSER_* définies dans ton .env pour créer automatiquement ton accès admin sans interaction requise.

🧭 Workflow au quotidien avec make

Plus besoin de naviguer dans les dossiers ou d'activer des environnements virtuels locaux (venv). Tout passe par les commandes du Makefile.
Lancement et Arrêt
Bash

# Lancer l'application en arrière-plan
make up

# Arrêter l'application
make down

# Reconstruire les images (après un changement de requirements.txt ou package.json)
make build

# Voir l'état des services
make status

📋 Logs et Débogage
Bash

# Logs de tous les services en continu
make logs

# Logs spécifiques par service
make logs-b     # Backend (Django)
make logs-f     # Frontend (Vue.js)
make logs-db    # Base de données (PostgreSQL)

🗄️ Base de données & Django
Bash

# Appliquer manuellement les migrations
make migrate

# Injecter les catégories initiales
make seed

# Créer un super-utilisateur manuellement si besoin
make db-su

🐚 Accès direct aux Conteneurs (Shell)
Bash

# Entrer dans le conteneur Backend
make ct-b

# Entrer dans le conteneur Frontend
make ct-f

# Ouvrir un terminal SQL (psql) directement sur la base de données
make ct-db

🌐 Accès aux services
Service	URL / Connexion	Description
Frontend	http://localhost:5173	Interface Vue.js (avec rechargement à chaud)
Backend (API)	http://localhost:8000	API Django
Admin Django	http://localhost:8000/admin	Interface d'administration
BDD (Client SQL externe)	localhost:5432	PostgreSQL (DBeaver, TablePlus, pgAdmin...)
💾 Gestion et réinitialisation des données

Les données PostgreSQL sont persistées dans le volume Docker nommé pgdata.

Si tu as besoin de réinitialiser complètement ton environnement à cause de migrations corrompues ou pour repartir de zéro :

# ⚠️ Supprime les conteneurs ET toutes les données de la base
make clean-v

# Relancer proprement
make setup

🐛 Dépannage courant
Problème	Cause	Solution
Port 8000 or 5173 already allocated	Un ancien processus tourne encore sur ta machine.	Utilise make down ou tue le processus bloquant le port.
Nouveau package Python / Node non détecté	L'image Docker n'a pas les nouvelles dépendances.	Ajoute le package dans requirements.txt ou package.json et lance make build.
Erreur de connexion DB au démarrage	Django démarre trop vite avant que PostgreSQL soit prêt.	Le healthcheck est configuré dans le docker-compose.yml pour forcer Django à attendre la disponibilité réelle de la BDD.