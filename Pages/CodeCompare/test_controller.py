import tkinter
import unittest
from unittest.mock import MagicMock, patch

from Pages.CodeCompare import controller


class Test_Code_Compare_Controller(unittest.TestCase):

    @patch("Tools.FileSingleton.FileSingleton", new_callable=MagicMock)
    def setUp(self, mock_singleton):
        self.mock_singleton = mock_singleton
        self.mock_view = MagicMock()
        self.mock_view.singleton = self.mock_singleton
        self.mock_view.right_output_preview = MagicMock()
        self.mock_view.left_output_preview = MagicMock()
        self.mock_view.toplevel_window = MagicMock()
        self.mock_view.output_button = MagicMock()
        self.mock_view.output_frame = MagicMock()
        self.mock_view.infile_preview = MagicMock()
        self.mock_view.run_button = MagicMock()
        self.mock_view.infile_button = MagicMock()
        self.mock_view.infile_label = MagicMock()
        self.mock_view.infile_frame = MagicMock()
        self.mock_view.checkbox = MagicMock()
        self.mock_view.checkbox_vars = MagicMock()
        self.mock_view.second_file_name = MagicMock()
        self.mock_view.import_second_source_button = MagicMock()
        self.mock_view.import_second_source_label = MagicMock()
        self.mock_view.first_file_name = MagicMock()
        self.mock_view.import_first_source_button = MagicMock()
        self.mock_view.import_first_source_label = MagicMock()
        self.mock_view.import_file_frame = MagicMock()

        self.controller = controller.Controller(self.mock_view)

    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.cpp")
    @patch('builtins.open', new_callable=MagicMock)
    def test_load_source_file_load_first_file(self, mock_file_dialog, mock_open):
        self.controller.load_source_file(0)

        self.assertEqual(self.mock_view.import_first_source_button._bg_color, "green")
        self.assertEqual(self.controller.first_path, "path/test.cpp")
        self.mock_view.first_file_name.configure.assert_called_once_with(text="test.cpp")
        self.mock_singleton._FileSingleton__instance.set_file.assert_called_once_with("path/test.cpp", 0)

    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.cpp")
    @patch('builtins.open', new_callable=MagicMock)
    def test_load_source_file_load_first_does_not_changes_secod(self, mock_file_dialog, mock_open):
        color = self.mock_view.import_second_source_button._bg_color
        path = self.controller.second_path

        self.controller.load_source_file(0)

        self.assertEqual(self.mock_view.import_second_source_button._bg_color, color)
        self.assertEqual(self.controller.second_path, path)
        self.mock_view.second_file_name.configure.assert_not_called()

    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.cpp")
    @patch('builtins.open', new_callable=MagicMock)
    def test_load_source_file_load_second_file(self, mock_file_dialog, mock_open):
            self.controller.load_source_file(1)

            self.assertEqual(self.mock_view.import_second_source_button._bg_color, "green")
            self.assertEqual(self.controller.second_path, "path/test.cpp")
            self.mock_view.second_file_name.configure.assert_called_once_with(text="test.cpp")
            self.mock_singleton._FileSingleton__instance.set_file.assert_called_once_with("path/test.cpp", 1)

    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.cpp")
    @patch('builtins.open', new_callable=MagicMock)
    def test_load_source_file_load_second_does_not_changes_first(self, mock_file_dialog, mock_open):
        color = self.mock_view.import_first_source_button._bg_color
        path = self.controller.first_path

        self.controller.load_source_file(1)

        self.assertEqual(self.mock_view.import_first_source_button._bg_color, color)
        self.assertEqual(self.controller.first_path, path)
        self.mock_view.first_file_name.configure.assert_not_called()

    @patch('builtins.open', new_callable=MagicMock)
    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.txt")
    def test_open_proper_testcase_path(self, mock_file_dialog, mock_open):
        mock_open.return_value.read.return_value = "test" \
                                                   "" \
                                                   "" \
                                                   "abcxyz"
        self.controller.open_testcase_file()

        self.assertEqual(self.controller.path, "path/test.txt")
        self.assertEqual(self.mock_view.infile_button._bg_color, "green")
        self.assertEqual(self.controller.input_text, "test"
                                                          ""
                                                          ""
                                                          "abcxyz")
        mock_open.return_value.close.assert_called_once()
        self.mock_view.infile_preview.delete.assert_called_once_with("0.0", tkinter.END)
        self.mock_view.infile_preview.insert.assert_called_once_with(tkinter.END, self.controller.input_text)

    @patch('tkinter.filedialog.askopenfilename', return_value="")
    def test_open_testcase_file_when_empty_testcase_path_do_nothing(self, mock_file_dialog):
        self.controller.open_testcase_file()

        self.mock_view.infile_preview.delete.assert_not_called()
        self.mock_view.infile_preview.insert.assert_not_called()

    @patch('builtins.open', new_callable=MagicMock)
    @patch('Tools.EfficiencyChecker.EfficiencyChecker', new_callable=MagicMock)
    def test_run_when_file_not_loaded_does_nothing(self, mock_efficiency_checker, mock_open):
        self.mock_singleton._FileSingleton__instance.get_file.return_value = None

        self.controller.run()

        self.mock_view.generate_output_frane.assert_not_called()

    @patch('builtins.open', new_callable=MagicMock)
    @patch('Tools.EfficiencyChecker.EfficiencyChecker', new_callable=MagicMock)
    def test_run_when_input_not_loaded_does_nothing(self, mock_efficiency_checker, mock_open):
        self.mock_singleton._FileSingleton__instance.get_file.return_value = "file"

        self.controller.run()

        self.mock_view.generate_output_frane.assert_not_called()

    @patch('builtins.open', new_callable=MagicMock)
    @patch('Tools.EfficiencyChecker.EfficiencyChecker', new_callable=MagicMock)
    def test_run_when_compilation_error_does_nothing(self, mock_efficiency_checker, mock_open):
        self.mock_singleton._FileSingleton__instance.get_file.return_value = "file"
        self.mock_singleton._FileSingleton__instance.get_filepath.return_value = "test.cpp"
        self.controller.input_text = "test"

        mock_efficiency_checker.check_logs.return_value = "error"

        self.controller.run()

        self.mock_view.generate_output_frane.assert_called_once()


    def test_update_code_changes_text_when_changed_file(self):
        self.mock_singleton._FileSingleton__instance.get_filename.side_effect = ["test.cpp", "test2.cpp"]

        self.controller.update_code(1)

        self.mock_view.first_file_name.configure.assert_called_once_with(text="test.cpp")
        self.mock_view.second_file_name.configure.assert_called_once_with(text="test2.cpp")

    def test_update_code_when_changed_to_unexisting_file_file_1_set_no_file(self):
        self.mock_singleton._FileSingleton__instance.get_filename.side_effect = ["", "test.cpp"]

        self.controller.update_code(1)

        self.mock_view.second_file_name.configure.assert_called_once_with(text="test.cpp")
        self.mock_view.first_file_name.configure.assert_called_once_with(text="No file")

    def test_update_code_when_changed_to_unexisting_file_file_2_set_no_file(self):
        self.mock_singleton._FileSingleton__instance.get_filename.side_effect = ["test.cpp", ""]

        self.controller.update_code(1)

        self.mock_view.first_file_name.configure.assert_called_once_with(text="test.cpp")
        self.mock_view.second_file_name.configure.assert_called_once_with(text="No file")



