import subprocess
import datetime
import os
from typing import Optional, IO
from Tools.FileSingleton import FileSingleton


class CppObject:
    __instance = FileSingleton.get_instance()

    # __code_filepath: Optional[str] = None
    # __id: Optional[int] = None
    #
    # __input: Optional[str] = None
    # __input_filepath: Optional[str] = None
    # __output: Optional[str] = None
    #
    # __compilation_logs: Optional[str] = None
    # __leaks_logs: Optional[str] = None
    # __max_execution_time: Optional[int] = None
    # __execution_time: Optional[int] = None

    def __init__(self, input_filepath: str, input: str, id: int, exec_time):
        self.__compilation_logs = None
        self.__execution_time = None
        self.__leaks_logs = None
        self.__output = None

        self.__input = input
        self.__input_filepath = input_filepath
        self.__max_execution_time = exec_time
        self.__id = id
        self.__code_filepath = self.__instance.get_filepath(id)

    def compile_and_run(self):
        self.__compilation_logs = self.__compile()

        # tu musi byc robiony drugi watek ktory usypia na execution time i
        # zabija kompilowanie zeby while true nie dzialalo

        if self.__compilation_logs == "":
            # run with given input and test execution time
            start = datetime.datetime.now()  # start timer
            res = subprocess.run(['./a.out'], capture_output=True, text=True, input=self.__input, check=True)
            os.remove("a.out")
            self.__output = res.stdout
            end = datetime.datetime.now()  # end timer
            self.__execution_time = int((end - start).total_seconds() * 1000)

    def __compile(self):
        res = subprocess.run(['g++', self.__code_filepath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return res.stdout.decode('utf-8')

    def save_output_to_file(self) -> IO:
        if self.__output is not None:
            output_file_name = self.__input_filepath[self.__input_filepath.rfind('/') + 1:self.__input_filepath.rfind('.')] + ".out"
            try:
                output_file = open(output_file_name, 'w+')
                output_file.write(self.__output)
                output_file.close()
                return output_file
            except Exception as e:
                raise e

    def check_leaks(self):
        # check for leaks only, if compilation was successful
        if self.__compilation_logs == "":
            self.__leaks_logs = self.__run_leaks_test()

    def __run_leaks_test(self):
        # program needs to be compiled
        command = 'leaks -atExit -- ./a.out <' + str(self.__input_filepath) + '| grep LEAK'
        res = subprocess.run(command, text=True, capture_output=True, shell=True)
        os.remove("a.out")
        return res.stdout

    def get_leaks_logs(self):
        return self.__leaks_logs

    # execution time in ms
    def get_execution_time(self) -> int:
        return self.__execution_time

    def get_output(self) -> str:
        return self.__output

    # if function return nothing, compilation was successful
    def get_compilation_logs(self) -> str:
        return self.__compilation_logs
