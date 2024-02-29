import threading
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import SessionNotCreatedException

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
            driver.refresh()
    except SessionNotCreatedException as e:
        print("Erreur de session : ", e)
    finally:
        if driver:
            driver.quit()


def start_refreshing(urls, refresh_time):
    global threads
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
