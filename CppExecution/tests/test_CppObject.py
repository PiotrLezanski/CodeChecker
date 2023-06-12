import os
import signal
import subprocess
import unittest
from unittest.mock import MagicMock, patch
from CppExecution.CppObject import CppObject


class test_CppObject(unittest.TestCase):
    @patch("builtins.open", new_callable=MagicMock)
    @patch("Tools.FileSingleton.FileSingleton", new_callable=MagicMock)
    def setUp(self, mock_open, mock_singleton):
        _id = 0
        input_filepath = mock_open.return_value.open
        input_text = "1"
        exec_time = 1
        mock_singleton.get_filepath.return_value = "/file/path"

        self.instance = CppObject(_id, input_filepath, input_text, exec_time)

    def test_should_initialize_when_all_args_given(self):
        self.assertIsInstance(self.instance, CppObject)

    def test_should_compile_when_proper_code_given(self):
        with open("test.cpp", "w") as file:
            file.write("""
            #include <iostream>
            
            int main(){
                std::cout<<"test";
            }
            """)

        self.instance.code_filepath = "test.cpp"
        output = self.instance.compile()

        self.assertEqual(output, "")
        os.remove("test.cpp")

    def test_should_not_compile_when_wrong_code_given(self):
        with open("test.cpp", "w") as file:
            file.write("it is not even a code")

        self.instance.code_filepath = "test.cpp"
        output = self.instance.compile()

        self.assertNotEqual(output, "")
        os.remove("test.cpp")

    def test_should_run_when_proper_code_given(self):
        with open("test.cpp", "w") as file:
            file.write("""
            #include <iostream>
            
            int main(){
                int a;
                std::cin >> a;
                std::cout << a;
            }
            """)

        self.instance.input = "420"
        self.instance.code_filepath = "test.cpp"
        self.instance.compile_and_run()

        self.assertEqual(self.instance.output, "420")
        self.assertTrue(self.instance.execution_time > 0)
        os.remove("test.cpp")

    @patch("subprocess.run", new_callable=MagicMock)
    def test_should_run_when_wrong_code_given(self, mock_run):
        self.instance.compile = MagicMock(return_value="error")

        self.instance.compile_and_run()

        mock_run.assert_not_called()

    def test_should_run_when_infinity_loop_given(self):
        with open("test.cpp", "w") as file:
            file.write("""
            #include <iostream>
            
            int main(){
                int a;
                std::cin >> a;
                while(true){
                    std::cout << a;
                }
            }
            """)

        self.instance.input = "420"
        self.instance.code_filepath = "test.cpp"

        self.instance.compile_and_run()

        self.assertEqual(self.instance.compilation_logs, "Time limit exceeded")
        # self.assertTrue(self.instance.exceededTime())
        os.remove("test.cpp")

    @patch("builtins.open", new_callable=MagicMock)
    def test_should_not_save_when_no_output(self, mock_open):
        self.instance.output = None
        self.instance.save_output_to_file()

        mock_open.assert_not_called()

    @patch("builtins.open", new_callable=MagicMock)
    def test_should_save_when_output(self, mock_write):
        self.instance.output = "output"
        self.instance.save_output_to_file()

        mock_write.assert_called_once()

    def test_should_return_true_when_time_exceeded(self):
        self.instance.get_execution_time = MagicMock(return_value=2)
        self.instance.max_execution_time = 1

        output = self.instance.exceededTime()

        self.assertTrue(output)

    def test_should_return_false_when_time_not_exceeded(self):
        self.instance.get_execution_time = MagicMock(return_value=1)
        self.instance.max_execution_time = 2

        output = self.instance.exceededTime()

        self.assertFalse(output)

    @patch("subprocess.run", new_callable=MagicMock)
    def test_run_leaks_test(self, mock_run):
        mock_result = MagicMock()
        mock_result.stdout = "Leaks output"
        mock_run.return_value = mock_result

        result = self.instance.run_leaks_test()

        self.assertEqual(result, "Leaks output")
        command = 'leaks -atExit -- ./a.out <' + str(self.instance.input_filepath) + '| grep LEAK'
        mock_run.assert_called_once_with(command, text=True, capture_output=True, shell=True)
