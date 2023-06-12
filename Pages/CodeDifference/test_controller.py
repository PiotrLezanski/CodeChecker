import unittest
import difflib
from unittest.mock import MagicMock, patch

from Pages.CodeDifference.controller import Controller
from Tools.FileSingleton import FileSingleton


class Test_Code_Difference_Controller(unittest.TestCase):
    @patch("Tools.FileSingleton.FileSingleton", new_callable=MagicMock)
    def setUp(self, mock_singleton):
        self.mock_singleton = FileSingleton.get_instance()

        self.mock_view = MagicMock()
        self.mock_view.output_preview = MagicMock()
        self.mock_view.toplevel_window = MagicMock()
        self.mock_view.output_button = MagicMock()
        self.mock_view.output_frame = MagicMock()
        self.mock_view.run_button = MagicMock()
        self.mock_view.check_label = MagicMock()
        self.mock_view.check_container = MagicMock()
        self.mock_view.second_file_name = MagicMock()
        self.mock_view.import_second_source_button = MagicMock()
        self.mock_view.import_second_source_label = MagicMock()
        self.mock_view.first_file_name = MagicMock()
        self.mock_view.import_first_source_button = MagicMock()
        self.mock_view.import_first_source_label = MagicMock()
        self.mock_view.import_file_frame = MagicMock()

        self.test_controller = Controller(self.mock_view)

    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.cpp")
    def test_should_load_first_when_proper_source_path_given(self, mock_filedialog):
        self.test_controller.load_source_file(0)

        self.mock_view.first_file_name.configure.assert_called_once_with(text="test.cpp")
        self.mock_singleton.set_file.assert_called_once_with("path/test.cpp", 0)

    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.cpp")
    def test_should_load_second_when_proper_source_path_given(self, mock_filedialog):
        self.test_controller.load_source_file(1)

        self.mock_view.second_file_name.configure.assert_called_once_with(text="test.cpp")
        self.mock_singleton.set_file.assert_called_once_with("path/test.cpp", 1)

    @patch('tkinter.filedialog.askopenfilename', return_value="")
    def test_should_do_nothing_when_wrong_source_path_given(self, mock_filedialog):
        self.test_controller.load_source_file(0)

        self.mock_view.first_file_name.configure.assert_not_called()
        self.mock_view.second_file_name.configure.assert_not_called()

    @patch('tkinter.messagebox.showerror', new_callable=MagicMock)
    def test_should_do_not_run_when_both_files_none(self, mock_showerror):
        self.mock_singleton.get_file.return_value = None

        self.test_controller.run()

        self.test_controller.view.generate_output_frame.assert_not_called()

    @patch('tkinter.messagebox.showerror', new_callable=MagicMock)
    def test_should_do_not_run_when_only_first_file_none(self, mock_showerror):
        self.mock_singleton.get_file.side_effect = [None, 1]

        self.test_controller.run()

        self.test_controller.view.generate_output_frame.assert_not_called()

    @patch('tkinter.messagebox.showerror', new_callable=MagicMock)
    def test_should_do_not_run_when_only_second_file_none(self, mock_showerror):
        self.mock_singleton.get_file.side_effect = [1, None]

        self.test_controller.run()

        self.test_controller.view.generate_output_frame.assert_not_called()

    @patch('tkinter.messagebox.showerror', new_callable=MagicMock)
    def test_should_run_when_both_files_not_none(self, mock_showerror):
        mock_file = MagicMock()
        mock_file.readlines.side_effect = ["first", "second"]
        self.mock_singleton.get_file.return_value = mock_file
        self.mock_singleton.get_filepath.return_value = "path"

        self.test_controller.run()

        self.mock_view.generate_output_frame.assert_called_once()
