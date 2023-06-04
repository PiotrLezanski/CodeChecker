import unittest
from unittest.mock import MagicMock, patch

from Tools import FileSingleton
from Tools.Exceptions import WrongExtensionError


# if they'll tell me that we cant have two the same files open, I will test it

class TestFileSingleton(unittest.TestCase):
    def setUp(self):
        self.instance = FileSingleton.FileSingleton.get_instance()

    def tearDown(self):
        self.instance.reset()

    # Testing whether the singleton as a structure works correctly
    def test_get_instance(self):
        self.assertIsInstance(self.instance, FileSingleton.FileSingleton)

    def test_call_get_instance_twice(self):
        instance2 = FileSingleton.FileSingleton.get_instance()
        self.assertEqual(self.instance, instance2)

    def test_calling_constructor_directly(self):
        with self.assertRaises(Exception):
            FileSingleton.FileSingleton()

    # Testing whether files open correctly and throws exceptions when they should

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file1_with_invalid_extension(self, mock_open):
        invalid_file_path = 'test.txt'

        with self.assertRaises(WrongExtensionError):
            self.instance.set_file1(invalid_file_path)

        self.assertEqual(self.instance.get_filepath1(), None)
        self.assertEqual(self.instance.get_file1(), None)

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file2_with_invalid_extension(self, mock_open):
        invalid_file_path = 'test.txt'

        with self.assertRaises(WrongExtensionError):
            self.instance.set_file2(invalid_file_path)

        self.assertEqual(self.instance.get_filepath2(), None)
        self.assertEqual(self.instance.get_file2(), None)

    def test_set_unexisting_file1_path(self):
        unexisting_file_path = 'test.cpp'

        with self.assertRaises(FileNotFoundError):
            self.instance.set_file1(unexisting_file_path)

        self.assertEqual(self.instance.get_filepath1(), None)
        self.assertEqual(self.instance.get_file1(), None)

    def test_set_unexisting_file2_path(self):
        unexisting_file_path = 'test.cpp'

        with self.assertRaises(FileNotFoundError):
            self.instance.set_file2(unexisting_file_path)

        self.assertEqual(self.instance.get_filepath2(), None)
        self.assertEqual(self.instance.get_file2(), None)

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file1_with_valid_extension(self, mock_open):
        valid_file_path = 'test.cpp'

        self.instance.set_file1(valid_file_path)

        self.assertEqual(self.instance.get_filepath1(), valid_file_path)
        self.assertEqual(not mock_open.return_value.closed, False)

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file2_with_valid_extension(self, mock_open):
        valid_file_path = 'test.cpp'

        self.instance.set_file2(valid_file_path)

        self.assertEqual(self.instance.get_filepath2(), valid_file_path)
        self.assertEqual(not mock_open.return_value.closed, False)

    # Testing whether files close correctly

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file1_closes_previous_file(self, mock_open):
        valid_file_path = 'test.cpp'
        valid_file_path2 = 'test2.cpp'

        self.instance.set_file1(valid_file_path)
        self.instance.set_file1(valid_file_path2)

        self.assertEqual(mock_open.return_value.close.call_count, 1)

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file2_closes_previous_file(self, mock_open):
        valid_file_path = 'test.cpp'
        valid_file_path2 = 'test2.cpp'

        self.instance.set_file2(valid_file_path)
        self.instance.set_file2(valid_file_path2)

        self.assertEqual(mock_open.return_value.close.call_count, 1)

    # Testing opening new file when one is already open

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file1_with_valid_when_file1_already_open(self, mock_open):
        valid_file_path = 'test.cpp'
        valid_file_path2 = 'test2.cpp'

        self.instance.set_file1(valid_file_path)
        self.instance.set_file1(valid_file_path2)

        self.assertEqual(self.instance.get_filepath1(), valid_file_path2)
        self.assertEqual(mock_open.call_count, 2)

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file2_with_valid_when_file2_already_open(self, mock_open):
        valid_file_path = 'test.cpp'
        valid_file_path2 = 'test2.cpp'

        self.instance.set_file2(valid_file_path)
        self.instance.set_file2(valid_file_path2)

        self.assertEqual(self.instance.get_filepath2(), valid_file_path2)
        self.assertEqual(mock_open.call_count, 2)

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file1_with_invalid_path_when_file1_already_open(self, mock_open):
        valid_file_path = 'test.cpp'
        invalid_file_path = 'test.txt'

        self.instance.set_file1(valid_file_path)
        first_file = self.instance.get_file1()

        with self.assertRaises(WrongExtensionError):
            self.instance.set_file1(invalid_file_path)

        self.assertEqual(self.instance.get_filepath1(), valid_file_path)
        self.assertEqual(first_file, mock_open.return_value)  # compare before and after
        self.assertEqual(mock_open.call_count, 1)
        self.assertEqual(mock_open.return_value.close.call_count, 0)

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file2_with_invalid_path_when_file2_already_open(self, mock_open):
        valid_file_path = 'test.cpp'
        invalid_file_path = 'test.txt'

        self.instance.set_file2(valid_file_path)
        first_file = self.instance.get_file2()

        with self.assertRaises(WrongExtensionError):
            self.instance.set_file2(invalid_file_path)

        self.assertEqual(self.instance.get_filepath2(), valid_file_path)
        self.assertEqual(first_file, mock_open.return_value)  # compare before and after
        self.assertEqual(mock_open.call_count, 1)
        self.assertEqual(mock_open.return_value.close.call_count, 0)

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file1_with_unexisting_path_when_file1_already_open(self, mock_open):
        valid_file_path = 'test.cpp'
        unexisting_file_path = 'test2.cpp'

        self.instance.set_file1(valid_file_path)
        first_file = self.instance.get_file1()
        mock_open.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            self.instance.set_file1(unexisting_file_path)

        self.assertEqual(self.instance.get_filepath1(), valid_file_path)
        self.assertEqual(first_file, mock_open.return_value)  # compare before and after

    @patch('builtins.open', new_callable=MagicMock)
    def test_set_file2_with_unexisting_path_when_file2_already_open(self, mock_open):
        valid_file_path = 'test.cpp'
        unexisting_file_path = 'test2.cpp'

        self.instance.set_file2(valid_file_path)
        first_file = self.instance.get_file2()
        mock_open.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            self.instance.set_file2(unexisting_file_path)

        self.assertEqual(self.instance.get_filepath2(), valid_file_path)
        self.assertEqual(first_file, mock_open.return_value)  # compare before and after
