import tkinter as tk


def create_gui(start_callback, stop_callback):
    root = tk.Tk()
    root.title("Web Page Auto Refresh")

    main_frame = tk.Frame(root, padx=15, pady=15)
    main_frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(main_frame, text="Enter URLs:", font=("Helvetica", 12)).pack(anchor='w')

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

        # Si le bouton '+' existe déjà, le retirer avant d'en créer un nouveau
        if add_button is not None:  # Ajouter une vérification ici pour s'assurer que add_button n'est pas None
            add_button.pack_forget()

        # Créer un nouveau bouton '+' et le placer à côté du champ d'entrée
        add_button = tk.Button(url_entry_frame, text="+", font=("Helvetica", 12), command=add_url_entry)
        add_button.pack(side=tk.RIGHT)

    tk.Label(main_frame, text="Enter refresh time (seconds):", font=("Helvetica", 12)).pack(anchor='w')
    refresh_time_entry = tk.Entry(main_frame, width=20, font=("Helvetica", 12))
    refresh_time_entry.pack()

    start_button = tk.Button(main_frame, text="Start Refreshing", font=("Helvetica", 12),
                             command=lambda: start_callback(
                                 [entry.get() for entry in url_entries if entry.get()],
                                 refresh_time_entry.get()
                             ))
    start_button.pack(fill=tk.X, pady=5)

    stop_button = tk.Button(main_frame, text="Stop Refreshing", font=("Helvetica", 12), command=stop_callback)
    stop_button.pack(fill=tk.X)

    # Ajouter le premier champ d'entrée d'URL
    add_url_entry()

    return root
