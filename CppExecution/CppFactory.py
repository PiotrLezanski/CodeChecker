import os
from CppExecution.CppObject import *

class CppFactory:
    def __init__(self, max_exec_time : int):
        self.max_exec_time = max_exec_time
    
    # method receives C++ code as filepath and input as string
    def CppObjectFromFilepath(self, file_path : str, input_text : str):
        self.object = CppObject(file_path, input_text)
        self.object.compile_and_run()
        return self.object

    def exceededTime(self):
        if self.object.get_execution_time() < self.max_exec_time:
            return True
        else:
            return False