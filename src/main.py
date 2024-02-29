import json
import os
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import SessionNotCreatedException
import time
import threading
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

drivers = []
stop_event = threading.Event()

def refresh_page(url, refresh_time):
    driver = None
    try:
        edge_options = EdgeOptions()
        edge_service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=edge_service, options=edge_options)
        drivers.append(driver)  # Ajoutez le pilote à la liste des pilotes
        driver.get(url)

        while not stop_event.is_set():  # Utilisez l'événement stop pour vérifier l'arrêt
            time.sleep(refresh_time)
            driver.refresh()
    except SessionNotCreatedException as e:
        print("Erreur de session : ", e)
    finally:
        if driver:
            driver.quit()


def start_refreshing(urls, refresh_time):
    for url in urls:
        t = threading.Thread(target=refresh_page, args=(url, refresh_time))
        threads.append(t)
        t.start()


def stop_refreshing():
    stop_event.set()  # Déclenchez l'événement pour signaler aux threads de s'arrêter
    for driver in drivers:  # Quittez tous les pilotes
        driver.quit()
    for t in threads:  # Attendez que tous les threads se terminent
        t.join()


def get_config_path():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()


def create_gui():
    root = tk.Tk()
    root.title("Web Page Auto Refresh")

    main_frame = tk.Frame(root, padx=15, pady=15)  # Utilisez un cadre pour l'espacement
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Ajout d'un champ pour entrer l'URL
    tk.Label(main_frame, text="Enter URL:", font=("Helvetica", 12)).pack(anchor='w')
    url_entry = tk.Entry(main_frame, width=50, font=("Helvetica", 12))
    url_entry.pack()

    # Ajout d'un champ pour entrer le temps de rafraîchissement
    tk.Label(main_frame, text="Enter refresh time (seconds):", font=("Helvetica", 12)).pack(anchor='w')
    refresh_time_entry = tk.Entry(main_frame, width=20, font=("Helvetica", 12))
    refresh_time_entry.pack()

    # Ajout d'un bouton pour démarrer le rafraîchissement
    start_button = tk.Button(main_frame, text="Start Refreshing", font=("Helvetica", 12), command=lambda: start_refreshing([url_entry.get()], int(refresh_time_entry.get())))
    start_button.pack(fill=tk.X, pady=5)

    # Ajout d'un bouton pour arrêter le rafraîchissement
    stop_button = tk.Button(main_frame, text="Stop Refreshing", font=("Helvetica", 12), command=stop_refreshing)
    stop_button.pack(fill=tk.X)

    def on_close():
        stop_refreshing()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    root.mainloop()


if __name__ == '__main__':
    threads = []
    create_gui()
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
