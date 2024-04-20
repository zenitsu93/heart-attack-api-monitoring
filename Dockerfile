# Utiliser l'image Python officielle comme image de base
FROM python:3.10

# Définir le répertoire de travail dans le conteneur
WORKDIR /app


COPY . .

# Mettre à jour pip et installer les dépendances
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Define environment variable for Prometheus
ENV prometheus_multiproc_dir /tmp

# Définir la commande pour exécuter l'application
CMD ["uvicorn", "api_heart_attack_prediction:app", "--host", "0.0.0.0", "--port", "5000", "--log-level", "info", "--workers", "2"]

