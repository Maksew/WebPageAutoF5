# WebAutoF5 🔄

WebAutoF5 est une application Python 🐍 conçue pour rafraîchir automatiquement des pages web à intervalles réguliers. Elle utilise le navigateur Edge via Selenium pour ouvrir et rafraîchir les pages, et l'interface utilisateur est construite avec Tkinter.

## Fonctionnalités 🌟

- 🔄 Rafraîchissement automatique de plusieurs pages web simultanément à intervalles réguliers.
- ✅ Validation des URLs saisies par l'utilisateur pour s'assurer qu'elles sont valides avant de démarrer le rafraîchissement.
- 🖥️ Interface utilisateur graphique simple et intuitive pour démarrer et arrêter le rafraîchissement.
- 🚨 Gestion des erreurs et des exceptions, avec des messages d'erreur appropriés affichés à l'utilisateur.

## Installation 🔧

Avant de démarrer, assurez-vous d'avoir Python installé sur votre machine. Ensuite, installez toutes les dépendances nécessaires à l'aide du fichier `requirements.txt` fourni avec le projet :

```bash
pip install -r requirements.txt
```

Cette commande installera automatiquement toutes les bibliothèques et paquets Python nécessaires au bon fonctionnement de l'application.

## Utilisation 🛠️

Pour démarrer l'application, exécutez le script principal :

```bash
python main.py
```

Une fois l'application démarrée, suivez ces étapes :

1- Entrez l'URL ou les URLs que vous souhaitez rafraîchir dans les champs de saisie.
2- Spécifiez l'intervalle de temps (en secondes) entre chaque rafraîchissement dans le champ dédié.
3- Cliquez sur le bouton "Commencer le Rafraîchissement" pour démarrer le processus.
4- Pour arrêter le rafraîchissement, cliquez sur le bouton "Arrêter le Rafraîchissement".

## Architecture du projet 🏗️

```
WebAutoF5/
│
├── src/
│   ├── main.py                # Point d'entrée principal
│   ├── controller/            # Gère l'interaction entre UI et modèle
│   │   └── refresher_controller.py
│   ├── model/                 # Modèle de rafraîchissement des pages web
│   │   └── page_refresher.py
│   ├── view/                  # UI construit avec Tkinter
│   │   └── app_ui.py
│   └── logging_config.py      # Configuration des logs avec support couleur
│
├── tests/                     # Tests unitaires
│   ├── integration/
│   │   └── test_controller_model_integration.py
│   └── unit/
│       ├── test_app_ui.py
│       ├── test_page_refresher.py
│       └── test_refresher_controller.py
│
├── drivers/                   # Pilotes pour Selenium
│   └── msedgedriver.exe
│
├── docs/                      # Documentation et fichiers d'aide
│   └── documentation.pdf
│
└── venv/                      # Environnement virtuel Python
```

## Tests 🧪

Des tests unitaires sont fournis pour tester l'intégration entre le contrôleur, le modèle, et l'UI. Pour exécuter les tests, utilisez :

```bash
python -m unittest
```

## Contribution 🤝

Les contributions sont les bienvenues ! Soumettez vos pull requests à la branche principale.

