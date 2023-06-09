import unittest
from unittest.mock import MagicMock, patch
from Tools.EfficiencyChecker import EfficiencyChecker


class test_Efficiency_Checker(unittest.TestCase):
    @patch("builtins.open", new_callable=MagicMock)
    def setUp(self, mock_open):
        _id = 0
        mocked_filepath = mock_open.return_value.open
        self.instance = EfficiencyChecker(_id, mocked_filepath)

    @patch("builtins.open", new_callable=MagicMock)
    def test_should_initialize_when_all_args_given(self, mock_open):
        _id = 0
        mocked_filepath = mock_open.return_value.open
        max_time = 10_000

        expected_instance = EfficiencyChecker(_id, mocked_filepath, max_time)
        self.assertIsInstance(expected_instance, EfficiencyChecker)

    @patch("builtins.open", new_callable=MagicMock)
    def test_should_initialize_when_not_all_args_given(self, mock_open):
        _id = 0
        mocked_filepath = mock_open.return_value.open

        expected_instance = EfficiencyChecker(_id, mocked_filepath)
        self.assertIsInstance(expected_instance, EfficiencyChecker)

    def test_should_initialize_when_not_existing_path(self):
        _id = 0
        filepath = "/not/existing"

        with self.assertRaises(FileNotFoundError):
            EfficiencyChecker(_id, filepath)

    def test_should_return_correct_time_when_not_exceeded(self):
        self.instance.cpp_object.exceededTime = MagicMock(return_value=False)
        self.instance.cpp_object.get_execution_time = MagicMock(return_value=122)

        output = self.instance.check_time()
        self.assertEqual(output, "122 ms")

    def test_should_return_correct_string_when_exceeded(self):
        self.instance.cpp_object.exceededTime = MagicMock(return_value=True)

        output = self.instance.check_time()
        self.assertEqual(output, "Time limit exceeded")

    def test_should_return_leaks_when_exist(self):
        self.instance.cpp_object.check_leaks = MagicMock()
        self.instance.cpp_object.get_leaks_logs = MagicMock(return_value="i'm a leak")

        output = self.instance.check_leaks()
        self.assertEqual(output, "i'm a leak")

    def test_should_return_leaks_when_not_exist(self):
        self.instance.cpp_object.get_leaks_logs = MagicMock(return_value="")

        output = self.instance.check_leaks()
        self.assertEqual(output, "")

    def test_should_return_logs_when_exist(self):
        self.instance.cpp_object.get_compilation_logs = MagicMock(return_value="error")

        output = self.instance.check_logs()
        self.assertEqual(output, "error")

    def test_should_return_logs_when_not_exist(self):
        self.instance.cpp_object.get_compilation_logs = MagicMock(return_value="")

        output = self.instance.check_logs()
        self.assertEqual(output, "Compilation successful")
