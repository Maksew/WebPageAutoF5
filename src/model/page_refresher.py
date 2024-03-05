"""
Ce module contient la classe PageRefresher, conçue pour rafraîchir automatiquement
des pages web à intervalles réguliers. Elle utilise le navigateur Edge via Selenium
et webdriver-manager pour gérer automatiquement les sessions de navigateur.
Les pages sont rafraîchies dans des threads séparés pour permettre le rafraîchissement
simultané de plusieurs pages.
"""

import logging
import threading
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

logging.basicConfig(level=logging.INFO)


class PageRefresher:
    """Classe pour rafraîchir automatiquement des pages web à intervalles réguliers."""

    def __init__(self):
        self.drivers = []  # Liste pour stocker les instances de pilotes de navigateur.
        self.threads = []  # Liste pour stocker les threads de rafraîchissement.
        self.stop_event = threading.Event()  # Événement pour signaler l'arrêt des threads.

    def refresh_page(self, url, refresh_time):
        """
        Ouvre une page web dans un navigateur et la rafraîchit à intervalles réguliers.

        Args:
            url: L'URL de la page web à rafraîchir.
            refresh_time: L'intervalle de temps (en secondes) entre les rafraîchissements.
        """
        driver = None
        try:
            edge_options = EdgeOptions()
            edge_service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=edge_service, options=edge_options)
            self.drivers.append(driver)
            driver.get(url)

            while not self.stop_event.is_set():
                time.sleep(refresh_time)
                if self.stop_event.is_set():
                    break
                try:
                    driver.refresh()
                except WebDriverException:
                    logging.error("Le navigateur a été fermé ou a perdu la connexion.")
                    break
        except WebDriverException as e:
            logging.error("Erreur initiale de WebDriver : %s", e)
        finally:
            if driver:
                try:
                    driver.quit()
                except WebDriverException:
                    logging.error("Erreur lors de la tentative de fermer le navigateur.")

    def start_refreshing(self, urls, refresh_time):
        """
        Démarre le processus de rafraîchissement pour chaque URL fournie.

        Args:
            urls: Une liste d'URLs à rafraîchir.
            refresh_time: L'intervalle de temps (en secondes) entre les rafraîchissements.
        """
        self.stop_event.clear()
        self.threads = [threading.Thread(target=self.refresh_page,
                                         args=(url, refresh_time)) for url in urls]
        for thread in self.threads:
            thread.start()

    def stop_refreshing_async(self):
        """
        Arrête tous les processus de rafraîchissement de manière asynchrone.
        """

        def close_browsers():
            self.stop_event.set()
            time.sleep(1)
            while self.drivers:
                driver = self.drivers.pop()
                driver.quit()

        threading.Thread(target=close_browsers).start()
