# Utilisez l'image Python officielle avec Django préinstallé
FROM python:3.11

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers du projet dans le conteneur
COPY . /app

# Installez les dépendances
RUN pip install -r requirements.txt

# Exposez le port sur lequel votre application Django fonctionne
EXPOSE 8000

# Commande pour lancer votre application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
