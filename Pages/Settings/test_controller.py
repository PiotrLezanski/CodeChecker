import tkinter
import unittest
from unittest import mock
from unittest.mock import MagicMock, patch
from Pages.Settings import controller


class Test_Settings_Controller(unittest.TestCase):

    @patch("Tools.FileSingleton.FileSingleton", new_callable=MagicMock)
    def setUp(self, mock_singleton):
        self.mock_singleton = mock_singleton

        self.mock_view = MagicMock()
        self.mock_view.valuable_label = MagicMock()
        self.mock_view.slider = MagicMock()
        self.mock_view.generate_zoom_option = MagicMock()
        self.mock_view.generate_theme_switch = MagicMock()

        self.controller = controller.Controller(self.mock_view)

    @mock.patch("customtkinter.set_appearance_mode")
    def test_change_appearance_mode_to_dark(self, mock_ctk):
        val = MagicMock()
        val.get.return_value = "dark"
        self.controller.change_appearance_mode(val)

        mock_ctk.assert_called_once_with("dark")

    @mock.patch("customtkinter.set_appearance_mode")
    def test_change_appearance_mode_to_light(self, mock_ctk):
        val = MagicMock()
        val.get.return_value = "light"
        self.controller.change_appearance_mode(val)

        mock_ctk.assert_called_once_with("light")

    @mock.patch("customtkinter.set_widget_scaling")
    def test_change_window_scale(self, mock_ctk):
        self.controller.change_window_scale("100%")

        mock_ctk.assert_called_once_with(1.0)





