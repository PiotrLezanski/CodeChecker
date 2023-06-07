import os
from CppExecution.CppObject import CppObject
from Tools.Exceptions import WrongIdError
from Tools.FileSingleton import FileSingleton


class CppFactory:
    __default_max_exec_time = 15_000
    __instance = FileSingleton.get_instance()

    def __init__(self):
        self.__max_exec_time = None

    def create_cpp_object(self, id: int, input_filepath: str,
                                              max_exec_time=__default_max_exec_time):
        self.__max_exec_time = max_exec_time
        if id == 0 or id == 1:
            input_file = open(input_filepath, 'r')
            input_text = input_file.read()
            input_file.close()
            object = CppObject(input_filepath, input_text, id, max_exec_time)
            object.compile_and_run()
            return object
        else:
            raise WrongIdError("Wrong id given")

    #to ma byc robione przed skorzystaniem z cpp factory bo nie bede robic dwoch konstruktorow dla test casu!!!!!!!!!!
    # i check Effi tez to jest redundancja kodu i jest zla praktyka

    # def create_cpp_object_with_input_text(self, id: int, input_text: str, max_exec_time=__default_max_exec_time):
    #     if id == 0 or id == 1:
    #         code_filepath = self.__instance.get_filepath()
    #         input_filepath = code_filepath[0:code_filepath.rfind('/')] + "/CCtest.in"
    #         tmp_file = open(input_filepath, 'w+')
    #         tmp_file.write(input_text)
    #         tmp_file.close()
    #         return CppObject(input_filepath, input_text, id, max_exec_time)
    #     else:
    #         raise WrongIdError("Wrong id given")

    # def exceededTime(self):
    #     if self.object.get_execution_time() < self.__max_exec_time:
    #         return False
    #     else:
    #         return True


