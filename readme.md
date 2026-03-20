# 🛠️ ToolsUNeed — Guide de mise en place et d'utilisation

## 📋 Stack technique

| Composant | Technologie | Port |
|-----------|-------------|------|
| Base de données | PostgreSQL 16 | `5432` |
| Backend | Django (Python) | `8000` |
| Frontend | Vite / Node.js | `5173` |

---

## ⚙️ Prérequis

Avant de démarrer le projet, assurez-vous d'avoir installé :

- [Docker](https://www.docker.com/get-started) (v20+)
- [Docker Compose](https://docs.docker.com/compose/install/) (v2+)

Vérifiez vos versions :
```bash
docker --version
docker compose version
```

---

## 🚀 Mise en place du projet

### 1. Cloner le dépôt

```bash
git clone <url-du-repo>
cd <nom-du-projet>
```

### 2. Structure attendue du projet

```
.
├── docker-compose.yml
├── backend/
│   ├── Dockerfile
│   └── manage.py
└── frontend/
    ├── Dockerfile
    └── package.json
```

### 3. Démarrer les containers

```bash
# Construire et démarrer tous les services
docker compose up --build

# En arrière-plan (mode détaché)
docker compose up --build -d
```

### 4. Vérifier que tout fonctionne

```bash
docker compose ps
```

Tous les containers doivent afficher le statut `running`.

---

## 🌐 Accès aux services

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:5173 | Interface utilisateur |
| Backend (API) | http://localhost:8000 | API Django |
| Base de données | `localhost:5432` | PostgreSQL (via client SQL) |

---

## 🗄️ Informations de connexion — Base de données

| Paramètre | Valeur |
|-----------|--------|
| **Host** | `localhost` (depuis la machine hôte) ou `db` (depuis le backend) |
| **Port** | `5432` |
| **Nom de la BDD** | `toolsuneed` |
| **Utilisateur** | `myuser` |
| **Mot de passe** | `mypassword` |

Connexion via `psql` :
```bash
psql -h localhost -p 5432 -U myuser -d toolsuneed
```

---

## 🐳 Commandes Docker utiles

### Gestion des containers

```bash
# Démarrer les services
docker compose up -d

# Arrêter les services
docker compose down

# Arrêter ET supprimer les volumes (⚠️ perte des données BDD)
docker compose down -v

# Redémarrer un service spécifique
docker compose restart backend
```

### Logs

```bash
# Voir les logs de tous les services
docker compose logs

# Suivre les logs en temps réel
docker compose logs -f

# Logs d'un service spécifique
docker compose logs -f backend
docker compose logs -f frontend
docker compose logs -f db
```

### Exécuter des commandes dans un container

```bash
# Ouvrir un shell dans le backend
docker compose exec backend bash

# Ouvrir un shell dans la base de données
docker compose exec db psql -U myuser -d toolsuneed

# Ouvrir un shell dans le frontend
docker compose exec frontend sh
```

### Commandes Django (backend)

```bash
# Appliquer les migrations
docker compose exec backend python manage.py migrate

# Créer un superutilisateur
docker compose exec backend python manage.py createsuperuser

# Lancer les tests
docker compose exec backend python manage.py test

# Ouvrir le shell Django
docker compose exec backend python manage.py shell

# Créer de nouvelles migrations
docker compose exec backend python manage.py makemigrations
```

### Commandes Node.js (frontend)

```bash
# Installer un nouveau package
docker compose exec frontend npm install <package>

# Voir les logs du serveur Vite
docker compose logs -f frontend
```

---

## 🔄 Synchronisation des fichiers (Hot Reload)

Grâce aux volumes montés dans `docker-compose.yml`, toute modification locale est automatiquement reflétée dans les containers :

- `./backend` → `/app` dans le container backend (Django auto-reload activé)
- `./frontend` → `/app` dans le container frontend (Vite HMR activé)

**Aucun redémarrage nécessaire** pour les changements de code.

---

## 💾 Persistance des données

Les données PostgreSQL sont stockées dans le volume Docker nommé `pgdata`. Ce volume **persiste entre les redémarrages** des containers.

```bash
# Voir les volumes Docker
docker volume ls

# Inspecter le volume de données
docker volume inspect <nom-du-projet>_pgdata
```

> ⚠️ Pour réinitialiser complètement la base de données, utilisez `docker compose down -v` puis redémarrez.

---

## 🐛 Dépannage courant

| Problème | Solution |
|----------|----------|
| Port déjà utilisé | `lsof -i :PORT` puis tuer le processus, ou modifier le port dans `docker-compose.yml` |
| Erreur de connexion BDD | Attendre que le container `db` soit prêt avant le `backend` |
| Modules Python manquants | `docker compose build --no-cache backend` |
| Modules Node manquants | `docker compose exec frontend npm install` |
| Migrations en attente | `docker compose exec backend python manage.py migrate` |

---

## 📁 Variables d'environnement

Les variables sensibles sont définies directement dans `docker-compose.yml`. Pour un environnement de production, il est recommandé de les déplacer dans un fichier `.env` :

```env
POSTGRES_DB=toolsuneed
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
```

Et de référencer ce fichier dans `docker-compose.yml` avec `env_file: .env`.

> ⚠️ N'oubliez pas d'ajouter `.env` à votre `.gitignore` en production.