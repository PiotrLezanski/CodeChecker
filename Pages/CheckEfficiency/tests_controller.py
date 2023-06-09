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

        self.assertEqual(self.mock_view.import_source_button._bg_color, "green")
        self.mock_singleton._FileSingleton__instance.set_file.assert_called_once_with("path/test.cpp")
        self.mock_view.file_name.configure.assert_called_once_with(text="test.cpp")

    @patch('tkinter.filedialog.askopenfilename', return_value="")
    def test_load_source_file_when_empty_source_path_do_nothing(self, mock_file_dialog):
        self.mock_singleton.get_file.return_value = "test.cpp"

        self.test_controller.load_source_file()

        self.mock_view.file_name.configure.assert_not_called()
        self.mock_singleton._FileSingleton__instance.set_file.assert_not_called()

    @patch('builtins.open', new_callable=MagicMock)
    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.txt")
    def test_open_proper_testcase_path(self, mock_file_dialog, mock_open):
        mock_open.return_value.read.return_value = "test" \
                                                   "" \
                                                   "" \
                                                   "abcxyz"
        self.test_controller.open_testcase_file()

        self.assertEqual(self.test_controller.path, "path/test.txt")
        self.assertEqual(self.mock_view.infile_button._bg_color, "green")
        self.assertEqual(self.test_controller.input_text, "test"
                                                          ""
                                                          ""
                                                          "abcxyz")
        self.mock_view.infile_preview.delete.assert_called_once_with("0.0", tkinter.END)
        self.mock_view.infile_preview.insert.assert_called_once_with(tkinter.END, self.test_controller.input_text)

    @patch('tkinter.filedialog.askopenfilename', return_value="")
    def test_open_testcase_file_when_empty_testcase_path_do_nothing(self, mock_file_dialog):
        self.test_controller.open_testcase_file()

        self.mock_view.infile_preview.delete.assert_not_called()
        self.mock_view.infile_preview.insert.assert_not_called()

    def test_run_without_input_file_do_nothing(self):
        self.test_controller.run()

        self.mock_view.infile_preview.delete.assert_not_called()
        self.mock_view.infile_preview.insert.assert_not_called()




