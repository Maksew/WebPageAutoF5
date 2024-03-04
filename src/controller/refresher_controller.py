"""
Module contenant la classe RefresherController.

Ce module définit le contrôleur principal de l'application
de rafraîchissement automatique de pages web.
Il gère l'interaction entre la vue utilisateur et le modèle de rafraîchissement des pages,
fournissant les méthodes pour démarrer et arrêter le rafraîchissement des pages web.
"""

import logging
from tkinter import messagebox
import re

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
        """
        valid_urls = [url for url in urls if self.validate_url(url)]
        if len(valid_urls) != len(urls):
            invalid_urls = set(urls) - set(valid_urls)
            messagebox.showerror(
                "URL Invalide",
                "Les URLs suivantes ne sont pas valides:\n" + "\n".join(invalid_urls)
            )
            return

        try:
            refresh_time = float(refresh_time)
            if refresh_time <= 0:
                raise ValueError("Le temps de rafraîchissement doit être un nombre positif.")
            self.page_refresher.start_refreshing(valid_urls, refresh_time)
        except ValueError as e:
            messagebox.showerror(
                "Erreur de Temps de Rafraîchissement",
                str(e)
            )
            logging.error("Erreur de saisie: %s", e)

    @staticmethod
    def validate_url(url):
        regex = re.compile(
            r'^(https?://)?'  # http:// or https://
            r'((([A-Z0-9][A-Z0-9-]*\.)+[A-Z]{2,6})|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(:\d+)?(/.*)?$',  # optional port and path
            re.IGNORECASE)
        return re.match(regex, url) is not None

    def stop(self):
        """Arrête le processus de rafraîchissement des pages."""
        self.page_refresher.stop_refreshing_async()
