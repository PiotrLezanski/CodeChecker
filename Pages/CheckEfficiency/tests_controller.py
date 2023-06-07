import tkinter
import unittest
from unittest.mock import MagicMock, patch

from Pages.CheckEfficiency import controller


class Test_Check_Efficiency_Controller(unittest.TestCase):

    @patch("Tools.FileSingleton.FileSingleton", new_callable=MagicMock)
    def setUp(self, mock_singleton):
        self.mock_singleton = mock_singleton

        self.mock_view = MagicMock()
        self.mock_view.infile_preview = MagicMock()
        self.mock_view.infile_button = MagicMock()
        self.mock_view.infile_button._bg_color = MagicMock()
        self.mock_view.infile_preview.delete = MagicMock()
        self.mock_view.infile_preview.insert = MagicMock()
        self.mock_view.checkbox_vars = [MagicMock(), MagicMock(), MagicMock()]
        self.mock_view.checkbox_vars[0].get = MagicMock(return_value=1)
        self.mock_view.checkbox_vars[1].get = MagicMock(return_value=1)
        self.mock_view.checkbox_vars[2].get = MagicMock(return_value=1)
        self.mock_view.file_name = MagicMock()
        self.mock_view.file_name.configure = MagicMock()
        self.mock_view.import_source_button = MagicMock()
        self.mock_view.import_source_button._bg_color = MagicMock()

        self.test_controller = controller.Controller(self.mock_view)

    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.cpp")
    def test_load_proper_source_path(self, mock_file_dialog):
        self.test_controller.load_source_file()

        self.mock_view.file_name.configure.assert_called_once_with(text="test.cpp")
        self.assertEqual(self.mock_view.import_source_button._bg_color, "green")
        self.mock_singleton._FileSingleton__instance.set_file.assert_called_once_with("path/test.cpp")

    @patch('tkinter.filedialog.askopenfilename', return_value="")
    def test_load_empty_source_path(self, mock_file_dialog):
        self.test_controller.load_source_file()

        self.mock_view.file_name.configure.assert_not_called()
        self.mock_singleton._FileSingleton__instance.set_file.assert_not_called()



