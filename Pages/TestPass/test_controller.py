import unittest
import tkinter

import customtkinter
from unittest.mock import MagicMock, patch

import Tools.TestCase
from Pages.TestPass.controller import Controller
from Tools.FileSingleton import FileSingleton


class Test_Test_Pass_Controller(unittest.TestCase):
    @patch("Tools.FileSingleton.FileSingleton", new_callable=MagicMock)
    def setUp(self, mock_singleton):
        self.mock_singleton = FileSingleton.get_instance()

        self.mock_view = MagicMock()
        self.mock_view.testcases_frame = MagicMock()
        self.mock_view.run_all_button = MagicMock()
        self.mock_view.run_test_buttons = MagicMock()
        self.mock_view.output_texts = MagicMock()
        self.mock_view.output_labels = MagicMock()
        self.mock_view.separators = MagicMock()
        self.mock_view.input_texts = MagicMock()
        self.mock_view.input_labels = MagicMock()
        self.mock_view.testcase_frames = MagicMock()
        self.mock_view.number_of_tests = MagicMock()
        self.mock_view.toplevel_window = MagicMock()
        self.mock_view.file_name = MagicMock()

        self.test_controller = Controller(self.mock_view)

    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.cpp")
    def test_should_load_when_proper_source_path_given(self, mock_filedialog):
        self.test_controller.open_source_file()

        self.assertEqual(self.test_controller.code_filepath, "path/test.cpp")
        self.mock_view.file_name.configure.assert_called_once_with(text="test.cpp")
        self.mock_singleton.set_file.assert_called_once_with(self.test_controller.code_filepath)

    @patch('tkinter.filedialog.askopenfilename', return_value="")
    def test_should_do_nothing_when_wrong_source_path_given(self, mock_filedialog):
        self.test_controller.open_source_file()

        self.assertEqual(self.test_controller.code_filepath, "")
        self.mock_view.file_name.configure.assert_not_called()

    def test_should_load_tests_when_testcases_empty(self):
        self.mock_view.number_of_tests = None
        self.mock_view.test_number_entry.get = MagicMock(return_value="2")

        self.test_controller.load_tests()

        self.mock_view.create_testcase_components.assert_called_once()
        assert self.mock_view.generate_testcase_frame.call_count == 2

    def test_should_recreate_tests_when_already_there(self):
        self.mock_view.number_of_tests = 1
        self.mock_view.test_number_entry.get = MagicMock(return_value="3")

        self.test_controller.load_tests()

        self.mock_view.hide_testcases.assert_called_once()
        self.mock_view.create_testcase_components.assert_called_once()
        assert self.mock_view.generate_testcase_frame.call_count == 3

    @patch("tkinter.messagebox.showerror", new_callable=MagicMock)
    def test_should_display_messagebox_when_not_numeric_input(self, mock_showerror):
        self.mock_view.test_number_entry.get = MagicMock(return_value="six")

        self.test_controller.load_tests()

        mock_showerror.assert_called_once()
        self.mock_view.create_testcase_components.assert_not_called()

    @patch("tkinter.messagebox.showerror", new_callable=MagicMock)
    def test_should_display_messagebox_when_input_out_of_range(self, mock_showerror):
        self.mock_view.test_number_entry.get = MagicMock(return_value="-1")
        self.test_controller.load_tests()

        self.mock_view.test_number_entry.get = MagicMock(return_value="11")
        self.test_controller.load_tests()

        assert mock_showerror.call_count == 2
        self.mock_view.create_testcase_components.assert_not_called()

    # @patch("Tools.TestCase.TestCase.compare_output", return_value=True)
    # @patch("Tools.TestCase.TestCase.get_compilation_logs", return_value="")
    # def test_should_create_testcase_when_no_compilation_logs_and_test_passed(self,
    #                                                                          mock_get_compilation_logs,
    #                                                                          mock_compare_output):
    #     self.mock_singleton.get_default.return_value = 0
    #     self.mock_view.input_texts[1].get.return_value = "input"
    #     self.mock_view.output_texts[1].get.return_value = "output"
    #
    #     self.test_controller.create_testcase(1)
    #
    #     assert self.test_controller.generated_output == "Test 2: PASSED"

    # @patch("Tools.TestCase.TestCase.get_output", return_value="expected")
    # @patch("Tools.TestCase.TestCase.compare_output", return_value=False)
    # @patch("Tools.TestCase.TestCase.get_compilation_logs", return_value="")
    # def test_should_create_testcase_when_no_compilation_logs_and_test_passed(self,
    #                                                                          mock_get_compilation_logs,
    #                                                                          mock_compare_output, mock_get_output):
    #     self.mock_singleton.get_default.return_value = 0
    #     self.mock_view.input_texts[1].get.return_value = "input"
    #     self.mock_view.output_texts[1].get.return_value = "output"
    #
    #     self.test_controller.create_testcase(1)
    #
    #     assert self.test_controller.generated_output == "\nTest 2: NOT PASSED\nYour output:\noutput\nExpected output:\nexpected"

    def test_should_run_all_testcases(self):
        self.mock_view.number_of_tests = 6
        self.test_controller.create_testcase = MagicMock()
        self.test_controller.generated_output = ""

        self.test_controller.run_all_testcases()

        assert self.test_controller.create_testcase.call_count == 6

    @patch("customtkinter.CTkTextbox", new_callable=MagicMock)
    @patch("customtkinter.CTkToplevel", new_callable=MagicMock)
    def test_should_create_toplevel_when_first_called(self, mock_toplevel, mock_textbox):
        self.mock_view.toplevel_window = None

        self.test_controller.open_preview_window("result")

        self.mock_view.output_preview.delete.assert_called_once_with("0.0", tkinter.END)
        self.mock_view.output_preview.insert.assert_called_once_with("0.0", "result")

    @patch("customtkinter.CTkTextbox", new_callable=MagicMock)
    @patch("customtkinter.CTkToplevel", new_callable=MagicMock)
    def test_should_display_toplevel_when_already_created(self, mock_toplevel, mock_textbox):
        self.test_controller.open_preview_window("result")

        self.mock_view.toplevel_window.focus.assert_called_once()
