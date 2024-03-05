import unittest
from unittest.mock import Mock, patch
from controller.refresher_controller import RefresherController


class TestRefresherController(unittest.TestCase):

    def setUp(self):
        """Initialise les ressources pour chaque test."""
        self.controller = RefresherController()

    def test_start(self):
        """Teste le démarrage du rafraîchissement."""
        urls = ['https://example.com']
        refresh_time = '5'

        self.controller.page_refresher.start_refreshing = Mock()
        self.controller.start(urls, refresh_time)

        self.controller.page_refresher.start_refreshing.assert_called_once_with(urls, 5.0)

    def test_start_invalid_refresh_time(self):
        """Teste le démarrage avec un temps de rafraîchissement invalide."""
        urls = ['https://example.com']
        refresh_time = 'invalid'

        with self.assertLogs(level='ERROR'):
            self.controller.start(urls, refresh_time)

    def test_stop(self):
        """Teste l'arrêt du rafraîchissement."""
        self.controller.page_refresher.stop_refreshing_async = Mock()
        self.controller.stop()

        self.controller.page_refresher.stop_refreshing_async.assert_called_once()

    def test_run(self):
        """Teste l'exécution de l'interface utilisateur."""
        with patch.object(self.controller.view, 'mainloop') as mock_mainloop:
            self.controller.run()

        mock_mainloop.assert_called_once()

    def tearDown(self):
        """Nettoie les ressources après chaque test."""
        self.controller.view.destroy()
        del self.controller


if __name__ == '__main__':
    unittest.main()
