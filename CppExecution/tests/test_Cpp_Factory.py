import unittest
from unittest.mock import MagicMock, patch
from CppExecution.CppFactory import CppFactory


class Test_Cpp_Factory(unittest.TestCase):

    def setUp(self):
        self.cpp_factory = CppFactory()
        self.cpp_factory.singleton = MagicMock()

    @patch('builtins.open', new_callable=MagicMock)
    @patch('CppExecution.CppObject.CppObject.compile_and_run', new_callable=MagicMock)
    def test_create_cpp_object_from_filepath(self, mock_compile_and_run, mock_open):
        mock_open.return_value.read.return_value = "test"

        self.cpp_factory.create_cpp_object_from_filepath(0, "test")

        mock_open.return_value.read.assert_called_once()
        mock_open.return_value.close.assert_called_once()

        mock_compile_and_run.assert_called_once()

    @patch('builtins.open', new_callable=MagicMock)
    @patch('CppExecution.CppObject.CppObject.compile_and_run', new_callable=MagicMock)
    def test_create_cpp_object_from_text(self, mock_compile_and_run, mock_open):
        mock_open.return_value.read.return_value = "test"

        self.cpp_factory.create_cpp_object_from_text(0, "test")

        mock_open.return_value.write.assert_called_once()
        mock_open.return_value.close.assert_called_once()

        mock_compile_and_run.assert_called_once()




