# 🛠️ ToolsUNeed — Guide de mise en place et d'utilisation

## 📋 Stack technique

| Composant | Technologie | Port |
|-----------|-------------|------|
| Base de données | PostgreSQL 16 | `5432` |
| Backend | Django (Python) | `8000` |
| Frontend | Vite / Vue.js | `5173` |

---

## 🧭 Choisir ton mode de travail

Selon ce sur quoi tu travailles, tu n'as pas besoin de tout lancer. Voici les trois modes du quotidien :

| Contexte | Ce que tu lances | Ce que tu laisses éteint |
|---|---|---|
| **Backend seul** (models, API, migrations) | PostgreSQL + Django | Frontend |
| **Frontend seul** (composants, UI) | Frontend + API mockée | PostgreSQL + Django |
| **Stack complète** (intégration, tests E2E) | Tout via Docker Compose | — |

---

## ⚙️ Prérequis

- [Docker](https://www.docker.com/get-started) (v20+) et [Docker Compose](https://docs.docker.com/compose/install/) (v2+)
- Python 3.11+ et `pip`
- Node.js 18+ et `npm`

```bash
docker --version
docker compose version
python --version
node --version
```

---

## 🗄️ Mode 1 — Backend seul (le plus courant en apprentissage)

Tu travailles sur les models Django, les migrations, l'API DRF. Le frontend ne t'intéresse pas pour l'instant.

### Démarrer uniquement PostgreSQL via Docker

```bash
# Lancer uniquement la base de données
docker compose up -d db

# Vérifier qu'elle tourne
docker compose ps db
```

### Activer l'environnement Python et lancer Django localement

```bash
cd backend

# Créer le virtualenv (une seule fois)
python -m venv .venv

# Activer le virtualenv
source .venv/bin/activate        # Mac / Linux
.venv\Scripts\activate           # Windows

# Installer les dépendances (une seule fois)
pip install -r requirements.txt

# Lancer le serveur Django
python manage.py runserver
```

Django tourne sur http://localhost:8000 et se connecte à PostgreSQL via Docker sur le port 5432.

### Commandes Django du quotidien

```bash
# Créer les fichiers de migration après modification d'un model
python manage.py makemigrations

# Appliquer les migrations en base
python manage.py migrate

# Créer un superutilisateur pour l'admin
python manage.py createsuperuser

# Ouvrir le shell Django (tester des requêtes ORM à la main)
python manage.py shell

# Lancer les tests
python manage.py test

# Voir les migrations disponibles et leur état
python manage.py showmigrations
```

### Arrêter la base de données

```bash
docker compose stop db
```

---

## 🎨 Mode 2 — Frontend seul

Tu travailles sur les composants Vue, le routing, le design. Pas besoin de backend qui tourne.

```bash
cd frontend

# Installer les dépendances (une seule fois)
npm install

# Lancer le serveur de développement Vite
npm run dev
```

Vue tourne sur http://localhost:5173 avec hot reload automatique.

> **Astuce** : Pour travailler sur le frontend sans backend, utilise des données mockées localement dans tes stores Pinia. Tu branches sur la vraie API plus tard.

### Commandes frontend utiles

```bash
# Vérifier les erreurs TypeScript et lint
npm run lint

# Build de production (pour tester le rendu final)
npm run build

# Prévisualiser le build de production
npm run preview

# Installer un nouveau package Vue
npm install <nom-du-package>
```

---

## 🐳 Mode 3 — Stack complète via Docker

Tu veux tout faire tourner ensemble : tester l'intégration frontend ↔ API ↔ base de données, ou travailler sur une machine sans Python/Node installés localement.

```bash
# Construire et démarrer tous les services
docker compose up --build

# En arrière-plan
docker compose up --build -d

# Vérifier que tout tourne
docker compose ps
```

### Commandes Django via Docker (mode stack complète)

```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py createsuperuser
docker compose exec backend python manage.py shell
docker compose exec backend python manage.py test
docker compose exec backend python manage.py showmigrations
```

### Commandes Node.js via Docker

```bash
# Installer un package depuis le container
docker compose exec frontend npm install <package>
```

---

## 🌐 Accès aux services

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:5173 | Interface Vue.js |
| Backend (API) | http://localhost:8000 | API Django |
| Admin Django | http://localhost:8000/admin | Interface d'administration |
| BDD (client SQL) | `localhost:5432` | PostgreSQL |

---

## 🗄️ Informations de connexion — Base de données

| Paramètre | Valeur |
|-----------|--------|
| Host | `localhost` (machine hôte) ou `db` (depuis le container backend) |
| Port | `5432` |
| Base | `toolsuneed` |
| Utilisateur | `myuser` |
| Mot de passe | `mypassword` |

```bash
# Se connecter directement à PostgreSQL
psql -h localhost -p 5432 -U myuser -d toolsuneed

# Depuis le container Docker
docker compose exec db psql -U myuser -d toolsuneed
```

---

## 📋 Logs et débogage

```bash
# Voir les logs de tous les services Docker
docker compose logs -f

# Logs d'un service spécifique
docker compose logs -f backend
docker compose logs -f frontend
docker compose logs -f db

# Ouvrir un shell dans un container
docker compose exec backend bash
docker compose exec frontend sh
```

---

## 💾 Gestion des données

Les données PostgreSQL sont dans le volume Docker `pgdata`. Elles persistent entre les redémarrages.

```bash
# Voir les volumes Docker
docker volume ls

# ⚠️ Réinitialiser complètement la BDD (supprime toutes les données)
docker compose down -v
docker compose up -d db
```

---

## 🔄 Workflow recommandé au quotidien

```
1. Tu travailles sur un model ou une API ?
   → docker compose up -d db
   → cd backend && source .venv/bin/activate
   → python manage.py runserver

2. Tu travailles sur un composant Vue ?
   → cd frontend && npm run dev

3. Tu testes l'intégration complète ?
   → docker compose up --build
```

---

## 🐛 Dépannage courant

| Problème | Solution |
|----------|----------|
| Port déjà utilisé | `lsof -i :PORT` puis tuer le processus, ou modifier le port dans `docker-compose.yml` |
| Django ne trouve pas la BDD | Vérifier que `docker compose up -d db` tourne bien (`docker compose ps`) |
| `ModuleNotFoundError` Python | Vérifier que le virtualenv est activé (`source .venv/bin/activate`) |
| Modules Node manquants | `npm install` dans le dossier `frontend/` |
| Migrations en attente | `python manage.py migrate` |
| Erreur CORS entre frontend et backend | Vérifier `CORS_ALLOWED_ORIGINS` dans `settings.py` |

---

## 📁 Variables d'environnement

Les variables sont dans `docker-compose.yml`. Pour un environnement de production, les déplacer dans un fichier `.env` :

```env
POSTGRES_DB=toolsuneed
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
SECRET_KEY=ta-clé-secrète-django
DEBUG=False
```

> ⚠️ Toujours ajouter `.env` au `.gitignore`. Ne jamais committer de secrets.