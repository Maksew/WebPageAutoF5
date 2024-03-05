import unittest
from unittest.mock import patch, MagicMock
from model.page_refresher import PageRefresher


class TestPageRefresher(unittest.TestCase):

    def setUp(self):
        """Initialise les ressources pour chaque test."""
        self.page_refresher = PageRefresher()

    @patch('src.model.page_refresher.threading.Thread')
    def test_start_refreshing(self, mock_thread):
        """Teste si le rafraîchissement commence correctement."""
        urls = ['https://example.com']
        refresh_time = 5
        self.page_refresher.start_refreshing(urls, refresh_time)
        self.assertEqual(mock_thread.call_count, len(urls))
        for call_args in mock_thread.call_args_list:
            call_kwargs = call_args[1]
            target = call_kwargs.get('target')
            self.assertIsNotNone(target)
            self.assertEqual(target.__name__, 'refresh_page')

    @patch('src.model.page_refresher.threading.Thread')
    def test_stop_refreshing_async(self, mock_thread):
        """Teste si le rafraîchissement s'arrête correctement."""
        mock_thread.return_value = MagicMock()
        self.page_refresher.stop_event.clear()
        self.page_refresher.stop_refreshing_async()
        mock_thread.assert_called_once()

    def tearDown(self):
        """Nettoie les ressources après chaque test."""
        del self.page_refresher


if __name__ == '__main__':
    unittest.main()