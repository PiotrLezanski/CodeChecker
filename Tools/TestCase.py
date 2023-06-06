from typing import Optional

import CppExecution.CppFactory as CppFactory
import CppExecution.CppObject as CppObject


class TestCase:
    __default_test_time = 1000

    __test_time: Optional[int] = None

    __cpp_object: Optional[CppObject] = None
    __expected_test_output: Optional[str] = None

    def __init__(self, code_filepath: str, test_input: str, expected_test_output: str, test_time=__default_test_time):
        self.__expected_test_output = expected_test_output
        self.__test_time = test_time
        cpp_factory = CppFactory.CppFactory(self.__test_time)
        self.__cpp_object = cpp_factory.CppObjectFromString(code_filepath, test_input)
        self.__cpp_object.compile_and_run()

    def get_output(self):
        return self.__cpp_object.output_text

    def compare_output(self):
        return self.__cpp_object.output_text == self.__expected_test_output

    def get_compilation_logs(self):
        return self.__cpp_object.compilation_logs
