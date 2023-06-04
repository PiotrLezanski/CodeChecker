import os
from CppExecution.CppObject import *

class CppFactory:
    def __init__(self, max_exec_time : int):
        self.max_exec_time = max_exec_time

    # method receives C++ code as filepath and input as string
    def CppObjectFromFilepath(self, code_filepath : str, input_filepath : str):
        self.object = CppObject(code_filepath, input_filepath)
        return self.object

    def exceededTime(self):
        if self.object.get_execution_time() < self.max_exec_time:
            return True
        else:
            return False

    def CppObjectFromString(self, code_filepath : str, input_text : str):
        tmp_file = open("CCtest.in", 'w')
        tmp_file.write(input_text)
        input_filepath = str(os.chdir()) + "/CCtest.in"
        self.object = CppObject(code_filepath, input_filepath)
        return self.object