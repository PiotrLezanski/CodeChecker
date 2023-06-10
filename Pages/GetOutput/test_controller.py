import unittest
import tkinter

import customtkinter
from unittest.mock import MagicMock, patch

from Pages.GetOutput.controller import Controller
from Tools.FileSingleton import FileSingleton


class Test_Get_Output_Controller(unittest.TestCase):
    @patch("Tools.FileSingleton.FileSingleton", new_callable=MagicMock)
    def setUp(self, mock_singleton):
        self.mock_singleton = FileSingleton.get_instance()

        self.mock_view = MagicMock()
        self.mock_view.controller = MagicMock()
        self.mock_view.output_label = MagicMock()
        self.mock_view.output_frame = MagicMock()
        self.mock_view.save_output_button = MagicMock()
        self.mock_view.preview_button = MagicMock()
        self.mock_view.toplevel_window = MagicMock()
        self.mock_view.singleton = MagicMock()
        self.mock_view.code_frame = MagicMock()
        self.mock_view.language_picker_label = MagicMock()
        self.mock_view.language_picker = MagicMock()
        self.mock_view.import_source_label = MagicMock()
        self.mock_view.import_source_button = MagicMock()
        self.mock_view.imported_file_name = MagicMock()
        self.mock_view.infile_frame = MagicMock()
        self.mock_view.infile_label = MagicMock()
        self.mock_view.infile_button = MagicMock()
        self.mock_view.run_button = MagicMock()
        self.mock_view.infile_preview = MagicMock()

        self.test_controller = Controller(self.mock_view)

    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.cpp")
    def test_should_load_when_proper_source_path_given(self, mock_filedialog):
        self.test_controller.open_source_file()

        self.assertEqual(self.test_controller.code_filepath, "path/test.cpp")
        self.assertEqual(self.test_controller.code_file_name, "test.cpp")
        self.mock_view.imported_file_name.configure.assert_called_once_with(text="test.cpp")
        self.mock_singleton.set_file.assert_called_once_with(self.test_controller.code_filepath)

    @patch('tkinter.filedialog.askopenfilename', return_value="")
    def test_should_do_nothing_when_wrong_source_path_given(self, mock_filedialog):
        self.test_controller.open_source_file()

        self.assertEqual(self.test_controller.code_filepath, "")
        self.mock_view.imported_file_name.configure.assert_not_called()

    @patch('builtins.open', new_callable=MagicMock)
    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.cpp")
    def test_should_load_when_proper_input_path_given(self, mock_filedialog, mock_open):
        mock_open.return_value.read.return_value = "example input"

        self.test_controller.open_input_file()

        self.assertEqual(self.test_controller.input_filepath, "path/test.cpp")
        self.assertEqual(self.test_controller.input_text, "example input")
        self.mock_view.infile_preview.delete.assert_called_once_with("0.0", tkinter.END)
        self.mock_view.infile_preview.insert.assert_called_once_with(tkinter.END, self.test_controller.input_text)

    @patch('builtins.open', new_callable=MagicMock)
    @patch('tkinter.filedialog.askopenfilename', return_value="")
    def test_should_do_nothing_when_wrong_input_path_given(self, mock_filedialog, mock_open):
        mock_open.return_value.read.return_value = "example input"

        self.test_controller.open_input_file()

        mock_open.assert_not_called()

    @patch("CppExecution.CppObject.CppObject", new_callable=MagicMock)
    @patch("CppExecution.CppFactory.CppFactory.create_cpp_object_from_filepath", new_callable=MagicMock)
    @patch('builtins.open', new_callable=MagicMock)
    def test_should_run_when_proper_code_and_proper_input_in_filepath(self, mock_open, mock_factory, mock_cpp_object):
        self.test_controller.input_filepath = "path/test.cpp"
        mock_factory.return_value = mock_cpp_object
        mock_cpp_object.get_compilation_logs.return_value = ""

        self.test_controller.run_code()

        mock_open.return_value.write.assert_called_once_with(self.test_controller.input_text)
        self.mock_view.generate_output_frame.assert_called_once_with(self.test_controller.cppobject)

    @patch("CppExecution.CppObject.CppObject", new_callable=MagicMock)
    @patch("CppExecution.CppFactory.CppFactory.create_cpp_object_from_text", new_callable=MagicMock)
    def test_should_run_when_proper_code_and_proper_input_in_textbox(self, mock_factory, mock_cpp_object):
        self.test_controller.input_filepath = ""
        mock_factory.return_value = mock_cpp_object
        mock_cpp_object.get_compilation_logs.return_value = ""

        self.test_controller.run_code()

        self.mock_view.generate_output_frame.assert_called_once_with(self.test_controller.cppobject)

    @patch("CppExecution.CppObject.CppObject", new_callable=MagicMock)
    @patch("CppExecution.CppFactory.CppFactory.create_cpp_object_from_filepath", new_callable=MagicMock)
    @patch('builtins.open', new_callable=MagicMock)
    def test_should__when_proper_code_and_proper_input_in_filepath(self, mock_open, mock_factory, mock_cpp_object):
        self.test_controller.input_filepath = "path/test.cpp"
        mock_factory.return_value = mock_cpp_object
        mock_cpp_object.get_compilation_logs.return_value = "error"

        self.test_controller.run_code()

        mock_open.return_value.write.assert_called_once_with(self.test_controller.input_text)
        self.mock_view.generate_output_frame.assert_not_called()
        self.mock_view.infile_preview.delete.assert_called_once_with("0.0", tkinter.END)
        self.mock_view.infile_preview.insert.assert_called_once_with("0.0", "Compilation error:\nerror")

    @patch("customtkinter.CTkTextbox", new_callable=MagicMock)
    @patch("customtkinter.CTkToplevel", new_callable=MagicMock)
    @patch("CppExecution.CppObject.CppObject", new_callable=MagicMock)
    def test_should_create_toplevel_when_first_called(self, mock_cpp_object, mock_toplevel, mock_textbox):
        self.mock_view.toplevel_window = None
        self.test_controller.cppobject = mock_cpp_object
        mock_cpp_object.get_output.return_value = "output"

        self.test_controller.open_preview_window()

        self.mock_view.output_preview.delete.assert_called_once_with("0.0", tkinter.END)
        self.mock_view.output_preview.insert.assert_called_once_with("0.0", "output")

    @patch("customtkinter.CTkTextbox", new_callable=MagicMock)
    @patch("customtkinter.CTkToplevel", new_callable=MagicMock)
    @patch("CppExecution.CppObject.CppObject", new_callable=MagicMock)
    def test_should_display_toplevel_when_already_created(self, mock_cpp_object, mock_toplevel, mock_textbox):
        self.test_controller.open_preview_window()

        self.mock_view.toplevel_window.focus.assert_called_once()
