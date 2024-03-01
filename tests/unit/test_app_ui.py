import unittest
import tkinter as tk
from unittest.mock import Mock
from src.view.app_ui import create_gui


class TestAppUi(unittest.TestCase):

    def setUp(self):
        """Initialise l'interface utilisateur pour les tests."""
        self.mock_start = Mock()
        self.mock_stop = Mock()
        self.root = create_gui(self.mock_start, self.mock_stop)
        self.root.update()  # Force la mise à jour de l'interface pour refléter les changements

    def test_initial_state(self):
        """Teste l'état initial du bouton de démarrage."""
        # Trouve tous les widgets Button dans main_frame
        buttons = [widget for widget in self.root.winfo_children()[0].winfo_children() if isinstance(widget, tk.Button)]

        # Vérifie l'état du bouton de démarrage par son texte
        start_button_texts = [button.cget('text') for button in buttons]
        self.assertIn("Commencer le Rafraîchissement", start_button_texts)

    def tearDown(self):
        """Ferme l'interface utilisateur après le test."""
        self.root.destroy()


if __name__ == '__main__':
    unittest.main()
