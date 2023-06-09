import os
from CppExecution.CppObject import CppObject
from Tools.Exceptions import WrongIdError
from Tools.FileSingleton import FileSingleton

class CppFactory:
    default_max_exec_time = 15_000
    def __init__(self, max_exec_time=default_max_exec_time):
        self.max_exec_time = max_exec_time
        self.singleton = FileSingleton.get_instance()

    def create_cpp_object_from_filepath(self, id: int, input_filepath: str, max_exec_time=default_max_exec_time):
        self.max_exec_time = max_exec_time
        if id == 0 or id == 1:
            input_file = open(input_filepath, 'r')
            input_text = input_file.read()
            input_file.close()
            cpp_object = CppObject(id, input_filepath, input_text, max_exec_time)
            cpp_object.compile_and_run()
            return cpp_object
        else:
            raise WrongIdError("Wrong id given")

    def create_cpp_object_from_text(self, id: int, input_text: str, max_exec_time=default_max_exec_time):
        if id == 0 or id == 1:
            code_filepath = self.singleton.get_filepath()
            input_filepath = code_filepath[0:code_filepath.rfind('/')] + "/CCtest.in"
            tmp_file = open(input_filepath, 'w+')
            tmp_file.write(input_text)
            tmp_file.close()
            cpp_object = CppObject(id, input_filepath, input_text, max_exec_time)
            cpp_object.compile_and_run()
            return cpp_object
        else:
            raise WrongIdError("Wrong id given")
