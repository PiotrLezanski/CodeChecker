import CppExecution.CppFactory as CppFactory
import CppExecution.CppObject as CppObject


class TestCase:
    __default_test_time = 1000

    __cpp_object = None
    __expected_test_output = None

    def __init__(self, code_filepath: str, test_input: str, expected_test_output: str, test_time=__default_test_time):
        self.__expected_test_output = expected_test_output
        cpp_factory = CppFactory.CppFactory(test_time)
        self.__cpp_object = cpp_factory.CppObjectFromString(code_filepath, test_input)
        self.__cpp_object.compile_and_run()

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
