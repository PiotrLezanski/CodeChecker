import subprocess
import datetime
import os
from typing import Optional, IO
from Tools.FileSingleton import FileSingleton

class CppObject:
    def __init__(self, id: int, input_filepath: str, input_text: str, exec_time):
        self.compilation_logs = ""
        self.execution_time = None
        self.leaks_logs = None
        self.output = None
        self.input = input_text
        self.input_filepath = input_filepath
        self.max_execution_time = exec_time
        self.id = id
        self.code_filepath = FileSingleton.get_instance().get_filepath(id)

    def compile_and_run(self):
        self.compilation_logs = self.compile()

        # tu musi byc robiony drugi watek ktory usypia na execution time i
        # zabija kompilowanie zeby while true nie dzialalo

        if self.compilation_logs == "":
            # run with given input and test execution time
            start = datetime.datetime.now()  # start timer
            res = subprocess.run(['./a.out'], capture_output=True, text=True, input=self.input, check=True)
            os.remove("a.out")
            self.output = res.stdout
            end = datetime.datetime.now()  # end timer
            self.execution_time = int((end - start).total_seconds() * 1000)

    def compile(self):
        res = subprocess.run(['g++', self.code_filepath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return res.stdout.decode('utf-8')

    def save_output_to_file(self) -> IO:
        if self.output is not None:
            output_file_name = self.input_filepath[self.input_filepath.rfind('/') + 1:self.input_filepath.rfind('.')] + ".out"
            try:
                output_filepath = self.code_filepath[0:self.code_filepath.rfind('/')+1:]+ str(output_file_name)
                output_file = open(output_filepath, 'w+')
                output_file.write(self.output)
                output_file.close()
                return output_file
            except Exception as e:
                raise e

    def check_leaks(self):
        # check for leaks only, if compilation was successful
        if self.compilation_logs == "":
            self.leaks_logs = self.run_leaks_test()

    def run_leaks_test(self):
        # program needs to be compiled
        command = 'leaks -atExit -- ./a.out <' + str(self.input_filepath) + '| grep LEAK'
        res = subprocess.run(command, text=True, capture_output=True, shell=True)
        return res.stdout

    def get_leaks_logs(self):
        return self.leaks_logs

    # execution time in ms
    def get_execution_time(self) -> int:
        return self.execution_time

    def get_output(self) -> str:
        return self.output

    # if function return nothing, compilation was successful
    def get_compilation_logs(self) -> str:
        return self.compilation_logs
