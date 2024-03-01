"""
Ce module fournit une interface utilisateur graphique pour
l'application de rafraîchissement automatique de pages web.

Il définit une fonction `create_gui` qui construit l'interface utilisateur à
l'aide de Tkinter et configure
les interactions nécessaires pour démarrer et arrêter le rafraîchissement des
pages web selon les URLs et
le temps de rafraîchissement spécifiés par l'utilisateur.
"""

import tkinter as tk
from tkinter import messagebox


def create_gui(start_callback, stop_callback):
    """
    Crée l'interface utilisateur pour l'application de rafraîchissement de pages web.

    Args:
        start_callback: Fonction à appeler pour démarrer le rafraîchissement.
        stop_callback: Fonction à appeler pour arrêter le rafraîchissement.
    """
    root = tk.Tk()
    root.title("Rafraîchissement Automatique de Page Web")

    # Cadre principal pour l'interface utilisateur.
    main_frame = tk.Frame(root, padx=15, pady=15)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Section pour l'entrée des URLs.
    tk.Label(main_frame, text="Entrez les URLs :", font=("Helvetica", 12)).pack(anchor='w')
    urls_frame = tk.Frame(main_frame)
    urls_frame.pack(fill=tk.BOTH, expand=True)
    url_entries = []  # Liste pour stocker les entrées d'URL.

    add_button = None

    # Fonction pour ajouter de nouvelles entrées d'URL.
    def add_url_entry():
        nonlocal add_button

        url_entry_frame = tk.Frame(urls_frame)
        url_entry_frame.pack(fill=tk.BOTH, expand=True)
        url_entry = tk.Entry(url_entry_frame, width=40, font=("Helvetica", 12))
        url_entry.pack(side=tk.LEFT, padx=(0, 10))
        url_entries.append(url_entry)

        if add_button is not None:
            add_button.pack_forget()

        add_button = tk.Button(url_entry_frame, text="+"
                               , font=("Helvetica", 12), command=add_url_entry)
        add_button.pack(side=tk.RIGHT)

    # Section pour l'entrée du temps de rafraîchissement.
    tk.Label(main_frame, text="Entrez le temps de rafraîchissement (secondes) :"
             , font=("Helvetica", 12)).pack(anchor='w')
    refresh_time_entry = tk.Entry(main_frame, width=20, font=("Helvetica", 12))
    refresh_time_entry.pack()

    # Fonction appelée lorsque le bouton de démarrage est pressé.
    def start_refreshing():
        urls = [entry.get() for entry in url_entries if entry.get().strip()]
        refresh_time_str = refresh_time_entry.get().strip()

        if not urls:
            messagebox.showwarning("Attention", "Veuillez saisir au moins une URL.")
            return

        try:
            refresh_time = float(refresh_time_str)
            if refresh_time <= 0:
                raise ValueError("Le temps de rafraîchissement doit être un nombre positif.")
        except ValueError:
            messagebox.showwarning("Attention", "Veuillez entrer un temps "
                                                "de rafraîchissement valide en secondes.")
            return

        start_callback(urls, refresh_time)

    # Boutons pour démarrer et arrêter le rafraîchissement.
    start_button = tk.Button(main_frame, text="Commencer le Rafraîchissement"
                             , font=("Helvetica", 12), command=start_refreshing)
    start_button.pack(fill=tk.X, pady=5)
    stop_button = tk.Button(main_frame, text="Arrêter le Rafraîchissement"
                            , font=("Helvetica", 12), command=stop_callback)
    stop_button.pack(fill=tk.X)

    add_url_entry()

    return root
