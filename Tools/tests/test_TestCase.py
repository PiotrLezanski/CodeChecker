import unittest
from unittest.mock import MagicMock, patch
from Tools import TestCase


class Test_TestCase(unittest.TestCase):
    def setUp(self):
        self.mock_cpp_object = MagicMock()
        self.mock_cpp_object.get_output.return_value = "Hello World"
        self.mock_cpp_factory = MagicMock()
        self.mock_cpp_factory.create_cpp_object_from_text.return_value = self.mock_cpp_object

        with patch('CppExecution.CppFactory.CppFactory', return_value=self.mock_cpp_factory):
            self.test_instance = TestCase.TestCase(1, "path/test.cpp", "Hello World")

    def test_change_expected_output(self):
        old_output = self.test_instance.get_expected_output()
        new_output = "Hello World!"

        self.test_instance.set_expected_output(new_output)

        self.assertEqual(self.test_instance.get_expected_output(), new_output)
        self.assertNotEqual(self.test_instance.get_expected_output(), old_output)

    def test_expected_outputs_equal(self):
        self.assertEqual(self.test_instance.get_output(), "Hello World")

    def test_expected_outputs_not_equal(self):
        self.test_instance.set_expected_output("Hello World!")
        self.assertEqual(self.test_instance.compare_output(), False)
