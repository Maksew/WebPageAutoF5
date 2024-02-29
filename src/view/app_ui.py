import tkinter as tk
from tkinter import messagebox

def create_gui(start_callback, stop_callback):
    root = tk.Tk()
    root.title("Rafraîchissement Automatique de Page Web")

    main_frame = tk.Frame(root, padx=15, pady=15)
    main_frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(main_frame, text="Entrez les URLs :", font=("Helvetica", 12)).pack(anchor='w')

    urls_frame = tk.Frame(main_frame)
    urls_frame.pack(fill=tk.BOTH, expand=True)

    url_entries = []
    add_button = None

    def add_url_entry():
        nonlocal add_button

        url_entry_frame = tk.Frame(urls_frame)
        url_entry_frame.pack(fill=tk.BOTH, expand=True)

        url_entry = tk.Entry(url_entry_frame, width=40, font=("Helvetica", 12))
        url_entry.pack(side=tk.LEFT, padx=(0, 10))
        url_entries.append(url_entry)

        if add_button is not None:
            add_button.pack_forget()

        add_button = tk.Button(url_entry_frame, text="+", font=("Helvetica", 12), command=add_url_entry)
        add_button.pack(side=tk.RIGHT)

    tk.Label(main_frame, text="Entrez le temps de rafraîchissement (secondes) :", font=("Helvetica", 12)).pack(anchor='w')
    refresh_time_entry = tk.Entry(main_frame, width=20, font=("Helvetica", 12))
    refresh_time_entry.pack()

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
            messagebox.showwarning("Attention", "Veuillez entrer un temps de rafraîchissement valide en secondes.")
            return

        start_callback(urls, refresh_time)

    start_button = tk.Button(main_frame, text="Commencer le Rafraîchissement", font=("Helvetica", 12),
                             command=start_refreshing)
    start_button.pack(fill=tk.X, pady=5)

    stop_button = tk.Button(main_frame, text="Arrêter le Rafraîchissement", font=("Helvetica", 12), command=stop_callback)
    stop_button.pack(fill=tk.X)

    add_url_entry()

    return root
