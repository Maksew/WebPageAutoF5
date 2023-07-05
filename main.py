from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
import threading


def refresh_page(url):
    driver = webdriver.Edge(service=Service('chemin_vers_le_pilote/msedgedriver.exe'))
    driver.get(url)

    while True:
        time.sleep(30)
        driver.refresh()


if __name__ == '__main__':
    urls = [
        'URL_1',
        'URL_2',
        # Ajoutez d'autres URL ici
    ]

    threads = []
    for url in urls:
        t = threading.Thread(target=refresh_page, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
