from prometheus_client import Counter, make_asgi_app

# Définition des compteurs Prometheus
survived_counter = Counter("survived", "Counter for survived predictions")
not_survived_counter = Counter("not_survived", "Counter for not survived predictions")

# Initialiser l'application de métriques Prometheus
metrics_app = make_asgi_app()
