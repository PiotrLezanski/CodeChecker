from typing import Optional

import CppExecution.CppFactory as CppFactory
import CppExecution.CppObject as CppObject


class TestCase:
    __default_test_time = 15_000
    __cpp_object: Optional[CppObject.CppObject] = None
    __expected_test_output: Optional[str] = None

    def __init__(self, id: int, input_filepath: str, expected_test_output: str, test_time=__default_test_time):
        self.__expected_test_output = expected_test_output
        cpp_factory = CppFactory.CppFactory()
        self.__cpp_object = cpp_factory.create_cpp_object(id, input_filepath, test_time)

    def get_output(self):
        return self.__cpp_object.get_output()

    def get_expected_output(self):
        return self.__expected_test_output

    def set_expected_output(self, expected_output: str):
        self.__expected_test_output = expected_output

    def compare_output(self):
        return self.__cpp_object.get_output() == self.__expected_test_output

    def get_compilation_logs(self):
        return self.__cpp_object.get_compilation_logs()
