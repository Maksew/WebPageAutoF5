import json
import os
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common import SessionNotCreatedException
import time
import threading
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService



def refresh_page(url, refresh_time):
    try:
        edge_options = EdgeOptions()
        edge_service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=edge_service, options=edge_options)
        driver.get(url)

        while True:
            time.sleep(refresh_time)
            driver.refresh()
    except SessionNotCreatedException as e:
        print("Erreur de session : ", e)
        print("Veuillez vous assurer que votre version de Microsoft Edge est compatible avec le WebDriver.")



def get_config_path():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()



if __name__ == '__main__':
    config_path = get_config_path()

    if config_path and os.path.isfile(config_path):
        with open(config_path, 'r') as f:
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
    else:
        print("Aucun chemin de fichier de configuration n'a été fourni.")
