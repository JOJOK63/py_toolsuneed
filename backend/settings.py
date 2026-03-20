DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "toolsuneed",
        "USER": "myuser",
        "PASSWORD": "mypassword",
        "HOST": "db",  # nom du service dans docker-compose
        "PORT": "5432",
    }
}