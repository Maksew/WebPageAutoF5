from ..model.page_refresher import start_refreshing, stop_refreshing_async
from ..view.app_ui import create_gui


class RefresherController:
    def __init__(self):
        self.view = create_gui(self.start, self.stop)

    def run(self):
        self.view.mainloop()

    def start(self, urls, refresh_time):
        refresh_time = int(refresh_time)
        start_refreshing(urls, refresh_time)

    def stop(self):
        stop_refreshing_async()