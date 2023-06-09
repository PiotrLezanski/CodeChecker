from Tools.FileSingleton import FileSingleton
from CppExecution import CppFactory
from CppExecution import CppObject


class EfficiencyChecker:

    def __init__(self, _id, input_text, max_exec_time=15_000):
        self.cpp_factory = CppFactory.CppFactory()
        self.cpp_object = self.cpp_factory.create_cpp_object_from_text(_id, input_text, max_exec_time)

    def check_time(self):
        if not self.cpp_object.exceededTime():
            return str(self.cpp_object.get_execution_time()) + " ms"
        else:
            return "Time limit exceeded"

    def check_leaks(self):
        if self.cpp_object.get_compilation_logs() == "":
            self.cpp_object.check_leaks()
            leaks = self.cpp_object.get_leaks_logs()
            return leaks if leaks != "" else "None"
        return "Compilation error"

    def check_logs(self):
        if self.cpp_object.get_compilation_logs() == "":
            return "Compilation successful"
        else:
            return self.cpp_object.get_compilation_logs()
