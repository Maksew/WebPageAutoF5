"""
Module contenant la classe RefresherController.

Ce module définit le contrôleur principal de l'application
de rafraîchissement automatique de pages web.
Il gère l'interaction entre la vue utilisateur et le modèle de rafraîchissement des pages,
fournissant les méthodes pour démarrer et arrêter le rafraîchissement des pages web.
"""

import logging
from src.view.app_ui import create_gui
from src.model.page_refresher import PageRefresher

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class RefresherController:
    """Classe contrôleur pour gérer l'application de rafraîchissement de pages."""

    def __init__(self):
        """Initialise le contrôleur avec le modèle de rafraîchissement de page et la vue UI."""
        self.page_refresher = PageRefresher()
        self.view = create_gui(self.start, self.stop)

    def run(self):
        """Exécute la boucle principale de l'interface utilisateur Tkinter."""
        self.view.mainloop()

    def start(self, urls, refresh_time):
        """
        Démarre le processus de rafraîchissement des pages.

        Args:
            urls: Une liste d'URL à rafraîchir.
            refresh_time: L'intervalle de temps pour le rafraîchissement des pages.
        """
        try:
            refresh_time = float(refresh_time)
            self.page_refresher.start_refreshing(urls, refresh_time)
        except ValueError:
            logging.error("Le temps de rafraîchissement doit être un nombre.")

    def stop(self):
        """Arrête le processus de rafraîchissement des pages."""
        self.page_refresher.stop_refreshing_async()
