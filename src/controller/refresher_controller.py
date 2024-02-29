import logging

from ..model.page_refresher import start_refreshing, stop_refreshing_async
from ..view.app_ui import create_gui


def start(urls, refresh_time):
    try:
        refresh_time = float(refresh_time)
        start_refreshing(urls, refresh_time)
    except ValueError:
        logging.error("Le temps de rafraîchissement doit être un nombre.")


def stop():
    stop_refreshing_async()


class RefresherController:
    def __init__(self):
        self.view = create_gui(start, stop)

    def run(self):
        self.view.mainloop()

