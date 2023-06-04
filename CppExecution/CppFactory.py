import os
import CppObject

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

    # method receives C++ code as string and input as string
    # def CppObjectFromString(self, code : str, input : str):
    #     temp_file = open('tempCodeChecker.in', 'w+')
    #     temp_file.write(code)
    #     current_directory = os.path.abspath(os.getcwd())
    #     self.object = CppObject(current_directory + "/tempCodeChecker.in", input)
    #     return object