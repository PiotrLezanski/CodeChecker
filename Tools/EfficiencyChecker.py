from Tools.FileSingleton import FileSingleton
from CppExecution import CppFactory
from CppExecution import CppObject


class EfficiencyChecker:
    def __init__(self):
        self.time_limit = 150000
        self.cpp_factory = CppFactory.CppFactory(self.time_limit)
        self.cpp_object = self.cpp_factory.CppObjectFromFilepath(FileSingleton.get_filepath1(), "TEST path")
        self.cpp_object.compile_and_run()

    def check_time(self):
        if not self.cpp_factory.exceededTime():
            return str(self.cpp_object.get_execution_time()) + " ms"
        else:
            return "Time limit exceeded"

    def check_leaks(self):
        self.cpp_object.check_leaks()
        return self.cpp_object.get_leaks_logs()

    def check_logs(self):
        if self.cpp_object.get_compilation_logs() == "":
            return "Compilation successful"
        else:
            return self.cpp_object.get_compilation_logs()
