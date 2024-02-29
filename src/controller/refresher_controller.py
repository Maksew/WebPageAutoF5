import logging
from src.view.app_ui import create_gui
from src.model.page_refresher import PageRefresher


class RefresherController:
    def __init__(self):
        self.page_refresher = PageRefresher()
        self.view = create_gui(self.start, self.stop)

    def run(self):
        self.view.mainloop()

    def start(self, urls, refresh_time):
        try:
            refresh_time = float(refresh_time)
            self.page_refresher.start_refreshing(urls, refresh_time)
        except ValueError:
            logging.error("Le temps de rafraîchissement doit être un nombre.")

    def stop(self):
        self.page_refresher.stop_refreshing_async()
