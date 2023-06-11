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
        self.mock_singleton._FileSingleton__instance.get_filename.return_value = "test.cpp"

        self.test_controller.load_source_file()

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
        self.assertEqual(self.test_controller.input_text, "test"
                                                          ""
                                                          ""
                                                          "abcxyz")
        mock_open.return_value.close.assert_called_once()
        self.mock_view.infile_preview.delete.assert_called_once_with("0.0", tkinter.END)
        self.mock_view.infile_preview.insert.assert_called_once_with(tkinter.END, self.test_controller.input_text)

    @patch('tkinter.filedialog.askopenfilename', return_value="")
    def test_open_testcase_file_when_empty_testcase_path_do_nothing(self, mock_file_dialog):
        self.test_controller.open_testcase_file()

        self.mock_view.infile_preview.delete.assert_not_called()
        self.mock_view.infile_preview.insert.assert_not_called()

    def test_run_without_source_file_do_nothing(self):
        self.mock_singleton._FileSingleton__instance.get_file.return_value = None

        self.test_controller.run()

        self.mock_view.infile_preview.delete.assert_not_called()
        self.mock_view.infile_preview.insert.assert_not_called()

    @patch("Tools.EfficiencyChecker.EfficiencyChecker", new_callable=MagicMock)
    def test_run_when_compile_error_show_logs(self, mock_efficiency_checker):
        self.mock_singleton._FileSingleton__instance.get_file.return_value = "test.cpp"
        self.mock_singleton._FileSingleton__instance.get_default.return_value = "0"
        self.test_controller.input_text = "text"
        mock_efficiency_checker.return_value.check_logs.return_value = "logs"

        self.test_controller.run()

        self.mock_view.generate_output_frame.assert_called_once_with("Logs: logs\n\n")

    @patch("Tools.EfficiencyChecker.EfficiencyChecker", new_callable=MagicMock)
    def test_run_when_compilation_successful_check_nothing(self, mock_efficiency_checker):
        self.mock_singleton._FileSingleton__instance.get_file.return_value = "test.cpp"
        self.mock_singleton._FileSingleton__instance.get_default.return_value = "0"
        self.test_controller.input_text = "text"
        mock_efficiency_checker.return_value.check_logs.return_value = "Compilation successful"
        self.mock_view.checkbox_vars[0].get.return_value = 0 #time
        self.mock_view.checkbox_vars[1].get.return_value = 0 #leaks
        self.mock_view.checkbox_vars[2].get.return_value = 0 #logs

        self.test_controller.run()

        self.mock_view.generate_output_frame.assert_called_once_with("Logs: Not checked\n\nTime: Not checked\n\nLeaks: Not checked\n\n")

    @patch("Tools.EfficiencyChecker.EfficiencyChecker", new_callable=MagicMock)
    def test_run_when_compilation_successful_check_time(self, mock_efficiency_checker):
        self.mock_singleton._FileSingleton__instance.get_file.return_value = "test.cpp"
        self.mock_singleton._FileSingleton__instance.get_default.return_value = "0"
        self.test_controller.input_text = "text"
        mock_efficiency_checker.return_value.check_logs.return_value = "Compilation successful"
        mock_efficiency_checker.return_value.check_time.return_value = "time"
        self.mock_view.checkbox_vars[0].get.return_value = 1  # time
        self.mock_view.checkbox_vars[1].get.return_value = 0  # leaks
        self.mock_view.checkbox_vars[2].get.return_value = 0  # logs

        self.test_controller.run()

        self.mock_view.generate_output_frame.assert_called_once_with(
            "Logs: Not checked\n\nTime: time\n\nLeaks: Not checked\n\n")

    @patch("Tools.EfficiencyChecker.EfficiencyChecker", new_callable=MagicMock)
    def test_run_when_compilation_successful_check_leaks(self, mock_efficiency_checker):
        self.mock_singleton._FileSingleton__instance.get_file.return_value = "test.cpp"
        self.mock_singleton._FileSingleton__instance.get_default.return_value = "0"
        self.test_controller.input_text = "text"
        mock_efficiency_checker.return_value.check_logs.return_value = "Compilation successful"
        mock_efficiency_checker.return_value.check_leaks.return_value = "leaks"
        self.mock_view.checkbox_vars[0].get.return_value = 0
        self.mock_view.checkbox_vars[1].get.return_value = 1
        self.mock_view.checkbox_vars[2].get.return_value = 0

        self.test_controller.run()

        self.mock_view.generate_output_frame.assert_called_once_with(
            "Logs: Not checked\n\nTime: Not checked\n\nLeaks: leaks\n\n")


    @patch("Tools.EfficiencyChecker.EfficiencyChecker", new_callable=MagicMock)
    def test_run_when_compilation_successful_check_logs(self, mock_efficiency_checker):
        self.mock_singleton._FileSingleton__instance.get_file.return_value = "test.cpp"
        self.mock_singleton._FileSingleton__instance.get_default.return_value = "0"
        self.test_controller.input_text = "text"
        mock_efficiency_checker.return_value.check_logs.return_value = "Compilation successful"
        self.mock_view.checkbox_vars[0].get.return_value = 0
        self.mock_view.checkbox_vars[1].get.return_value = 0
        self.mock_view.checkbox_vars[2].get.return_value = 1

        self.test_controller.run()

        self.mock_view.generate_output_frame.assert_called_once_with(
            "Logs: Compilation successful\n\nTime: Not checked\n\nLeaks: Not checked\n\n")

    def test_update_code_changes_text_when_changed_file(self):
        self.mock_singleton._FileSingleton__instance.get_filename.return_value = "test.cpp"

        self.test_controller.update_code(1)

        self.mock_view.file_name.configure.assert_called_once_with(text="test.cpp")

    def test_update_code_when_changed_to_unexisting_file_set_no_file(self):
        self.mock_singleton._FileSingleton__instance.get_filename.return_value = ""

        self.test_controller.update_code(1)

        self.mock_view.file_name.configure.assert_called_once_with(text="No file")



