import json
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
import threading


def refresh_page(url, refresh_time):
    driver = webdriver.Edge(service=Service(config['edge_driver_path']))
    driver.get(url)

    while True:
        time.sleep(refresh_time)
        driver.refresh()


if __name__ == '__main__':
    # Load configuration from file
    with open(r'your_file_path\config.json', 'r') as f:
        config = json.load(f)

    urls = config['urls']
    refresh_time = config['refresh_time']

    threads = []
    for url in urls:
        t = threading.Thread(target=refresh_page, args=(url, refresh_time))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
