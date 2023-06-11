import tkinter
import unittest
from unittest.mock import MagicMock, patch
from Pages.WelcomeWindow import controller


class Test_Welcome_Window_Controller(unittest.TestCase):

    @patch("Tools.FileSingleton.FileSingleton", new_callable=MagicMock)
    def setUp(self, mock_singleton):
        self.mock_singleton = mock_singleton

        self.mock_view = MagicMock()
        self.mock_view.checkboxes = [MagicMock(), MagicMock()]
        self.mock_view.text_boxes = [MagicMock(), MagicMock()]
        self.mock_view.content = MagicMock()
        self.mock_view.generate_message = MagicMock()
        self.mock_view.generate_code = MagicMock()
        self.mock_view.checkboxes[0].select = MagicMock()

        self.test_controller = controller.Controller(self.mock_view)

    @patch('tkinter.filedialog.askopenfilename', return_value="path/test.cpp")
    def test_load_file_when_proper_file_given_file_changes(self, mock_file_dialog):
        mock_label = MagicMock()
        mock_label.configure = MagicMock()
        test_name = "test.cpp"
        test_text = "test"
        self.mock_singleton._FileSingleton__instance.get_filename.return_value = test_name
        self.mock_singleton._FileSingleton__instance.get_file_text.return_value = test_text

        self.test_controller.load_file(1, mock_label)

        mock_label.configure.assert_called_once_with(text=test_name)
        self.mock_singleton._FileSingleton__instance.set_file.assert_called_once_with("path/test.cpp", 1)
        self.mock_view.text_boxes[1].delete.assert_called_once_with("0.0", tkinter.END)
        self.mock_view.text_boxes[1].insert.assert_called_once_with(tkinter.END, "test")
        self.mock_view.checkboxes[0].insert.assert_not_called()

    @patch('tkinter.filedialog.askopenfilename', return_value="")
    def test_load_file_file_does_not_change_if_empty_file_given(self, mock_file_dialog):
        mock_label = MagicMock()
        mock_label.configure = MagicMock()
        self.test_controller.load_file(1, mock_label)

        mock_label.configure.assert_not_called()
        self.mock_singleton._FileSingleton__instance.set_file.assert_not_called()
        self.mock_view.text_boxes[1].insert.assert_not_called()
        self.mock_view.checkboxes[0].insert.assert_not_called()

    def test_update_checkboxes_updates_checkboxes(self):
        self.test_controller.update_checkboxes(self.mock_view.checkboxes[1])

        self.mock_view.checkboxes[0].deselect.assert_called_once()
        self.mock_view.checkboxes[1].select.assert_called_once()
        self.mock_singleton._FileSingleton__instance.set_default.assert_called_once_with(1)

    def test_update_code_updates_checkboxes(self):
        self.mock_singleton._FileSingleton__instance.get_file_text.return_value = "test"

        self.test_controller.update_code(1)

        self.mock_view.text_boxes[1].insert.assert_called_once_with("0.0", "test")
        self.mock_view.checkboxes[0].insert.assert_not_called()




