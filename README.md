
1. **Installation des Prérequis**:
   - Installez Docker sur votre machine.
   - Assurez-vous que Python est installé.
   - Choisissez un IDE, comme PyCharm ou VSCode, et installez-le.

2. **Création de l'Image Docker pour l'API de Prédiction de Crise Cardiaque**:
   - Ouvrez un terminal et naviguez jusqu'au dossier de votre projet.
   - Exécutez la commande suivante pour construire l'image Docker :
     ```
     docker build -t heart_attack_prediction_api .
     ```

3. **Démarrage de l'Application en Mode Développement**:
   - Pour un débogage facile, il est recommandé de démarrer l'application via votre IDE (PyCharm ou VSCode).

4. **Démarrage de Prometheus et Grafana**:
   - Exécutez la commande suivante pour démarrer Prometheus et Grafana :
     ```
     docker compose up -d
     ```
   - Cette configuration est prête à fonctionner avec l'application lancée en mode développement.

5. **Accès à Prometheus et Grafana**:
   - Ouvrez un navigateur et accédez à Prometheus sur le port 9090.
   - Pour Grafana, accédez au port 3000. Utilisez "admin" comme nom d'utilisateur et "grafana" comme mot de passe.

6. **Surveillance des Métriques**:
   - Une fois dans Grafana, vous pouvez choisir les métriques à suivre, comme `not_survived_total` et `survived_total`.

En suivant ces étapes, vous serez en mesure de configurer et de surveiller efficacement votre application de prédiction de crises cardiaques, en utilisant Docker pour la gestion des conteneurs, Prometheus pour la surveillance des métriques, et Grafana pour la visualisation des données.