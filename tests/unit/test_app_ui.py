import unittest
import tkinter as tk
from unittest.mock import Mock
from view.app_ui import create_gui


class TestAppUi(unittest.TestCase):

    def setUp(self):
        """Initialise l'interface utilisateur pour les tests."""
        self.mock_start = Mock()
        self.mock_stop = Mock()
        self.root = create_gui(self.mock_start, self.mock_stop)
        self.root.update()

    def test_initial_state(self):
        """Teste l'état initial du bouton de démarrage."""
        buttons = [widget for widget in self.root.winfo_children()[0].winfo_children() if isinstance(widget, tk.Button)]

        start_button_texts = [button.cget('text') for button in buttons]
        self.assertIn("Commencer le Rafraîchissement", start_button_texts)

    def tearDown(self):
        """Ferme l'interface utilisateur après le test."""
        self.root.destroy()


if __name__ == '__main__':
    unittest.main()
