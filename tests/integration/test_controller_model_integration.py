import unittest
from unittest.mock import patch

from controller.refresher_controller import RefresherController


class TestControllerModelIntegration(unittest.TestCase):

    def setUp(self):
        """Setup resources before each test."""
        self.controller = RefresherController()

    @patch('controller.refresher_controller.PageRefresher.start_refreshing')
    def test_start_refreshing_integration(self, mock_start_refreshing):
        """Test controller and model integration to start page refreshing."""
        urls = ['https://example.com']
        refresh_time = 5
        self.controller.start(urls, refresh_time)
        mock_start_refreshing.assert_called_once_with(urls, refresh_time)

    @patch('controller.refresher_controller.PageRefresher.stop_refreshing_async')
    def test_stop_refreshing_integration(self, mock_stop_refreshing_async):
        """Test controller and model integration to stop page refreshing."""
        self.controller.stop()
        mock_stop_refreshing_async.assert_called_once()

    def tearDown(self):
        """Clean up resources after each test."""
        del self.controller


if __name__ == '__main__':
    unittest.main()
