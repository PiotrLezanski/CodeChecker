import os
from CppExecution.CppObject import *

class CppFactory:
    def __init__(self, max_exec_time : int):
        self.object = None
        self.max_exec_time = max_exec_time

    # method receives C++ code as filepath and input as string
    def CppObjectFromFilepath(self, code_filepath : str, input_filepath : str):
        self.object = CppObject(code_filepath, input_filepath)
        return self.object

    def exceededTime(self):
        if self.object.get_execution_time() < self.max_exec_time:
            return False
        else:
            return True

    def CppObjectFromString(self, code_filepath : str, input_text : str):
        input_file_filepath = code_filepath[0:code_filepath.rfind('/')] + "/CCtest.in"
        tmp_file = open(input_file_filepath, 'w+')
        tmp_file.write(input_text)
        tmp_file.close()
        self.object = CppObject(code_filepath, input_file_filepath)
        return self.object