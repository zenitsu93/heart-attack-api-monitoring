import joblib
import uvicorn
from fastapi import FastAPI
import pandas as pd
from fastapi.staticfiles import StaticFiles
from metrics import survived_counter, not_survived_counter, metrics_app

# Initialiser le modèle
heart_attack_model = joblib.load("./heart_attack_prediction_model.joblib")

app = FastAPI()

# Monter l'application de métriques Prometheus
app.mount("/metrics", metrics_app)

# Servir les fichiers statiques pour la page d'accueil
#app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/heart_attack")
def prediction_api(time: int, ejection_fraction: float, serum_creatinine: float):
    # Préparer les données pour la prédiction
    x = pd.DataFrame([[time, ejection_fraction, serum_creatinine]], columns=[
                     'time', 'ejection_fraction', 'serum_creatinine'])

    # Faire la prédiction
    prediction = heart_attack_model.predict(x)
    survived = int(prediction[0]) == 1

    # Incrémenter le compteur approprié
    if survived:
        survived_counter.inc()
    else:
        not_survived_counter.inc()

    return {"survived": survived}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
