import json
import os
import sys
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
import threading


def refresh_page(url, refresh_time, driver_path):
    driver = webdriver.Edge(service=Service(driver_path))
    driver.get(url)

    while True:
        time.sleep(refresh_time)
        driver.refresh()


def get_config_path():
    root = tk.Tk()
    root.withdraw()

    config_path = filedialog.askopenfilename()

    return config_path


if __name__ == '__main__':
    config_path = get_config_path()

    if config_path and os.path.isfile(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)

        urls = config['urls']
        refresh_time = config['refresh_time']

        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            driver_path = os.path.join(sys._MEIPASS, 'msedgedriver.exe')
        else:
            driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'msedgedriver.exe')

        threads = []
        for url in urls:
            t = threading.Thread(target=refresh_page, args=(url, refresh_time, driver_path))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
    else:
        print("Aucun chemin de fichier de configuration n'a été fourni.")
