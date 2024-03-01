import unittest
from unittest.mock import patch
from src.controller.refresher_controller import RefresherController


class TestControllerModelIntegration(unittest.TestCase):

    def setUp(self):
        """Initialise les ressources pour chaque test."""
        self.controller = RefresherController()

    @patch('src.model.page_refresher.PageRefresher.start_refreshing')
    def test_start_refreshing_integration(self, mock_start_refreshing):
        """Teste l'intégration entre le contrôleur et le modèle pour démarrer le rafraîchissement."""
        urls = ['https://example.com']
        refresh_time = 5
        self.controller.start(urls, refresh_time)
        mock_start_refreshing.assert_called_once_with(urls, refresh_time)

    @patch('src.model.page_refresher.PageRefresher.stop_refreshing_async')
    def test_stop_refreshing_integration(self, mock_stop_refreshing_async):
        """Teste l'intégration entre le contrôleur et le modèle pour arrêter le rafraîchissement."""
        self.controller.stop()
        mock_stop_refreshing_async.assert_called_once()

    def tearDown(self):
        """Nettoie les ressources après chaque test."""
        del self.controller


if __name__ == '__main__':
    unittest.main()
