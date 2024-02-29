import threading
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException
import logging

logging.basicConfig(level=logging.INFO)

drivers = []
threads = []
stop_event = threading.Event()


def refresh_page(url, refresh_time):
    driver = None
    try:
        edge_options = EdgeOptions()
        edge_service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=edge_service, options=edge_options)
        drivers.append(driver)
        driver.get(url)

        while not stop_event.is_set():
            time.sleep(refresh_time)
            if stop_event.is_set():
                break
            try:
                driver.refresh()
            except WebDriverException:
                logging.error("Le navigateur a été fermé ou a perdu la connexion.")
                break
    except WebDriverException as e:
        logging.error(f"Erreur initiale de WebDriver : {e}")
    finally:
        if driver:
            try:
                driver.quit()
            except WebDriverException:
                logging.error("Erreur lors de la tentative de fermer le navigateur.")


def start_refreshing(urls, refresh_time):
    global threads, stop_event
    stop_event.clear()
    threads = [threading.Thread(target=refresh_page, args=(url, refresh_time)) for url in urls]
    for thread in threads:
        thread.start()


def stop_refreshing_async():
    def close_browsers():
        stop_event.set()
        time.sleep(1)
        while drivers:
            driver = drivers.pop()
            driver.quit()
    threading.Thread(target=close_browsers).start()
