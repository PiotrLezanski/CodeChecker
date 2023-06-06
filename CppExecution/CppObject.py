import subprocess
import datetime
import os

class CppObject:
    def __init__(self, source_code_filepath, input_filepath):
        self.output_file_name = None
        self.leaks_logs = None
        self.output_text = None
        self.execution_time = None
        self.compilation_logs = ""
        self.file_path = source_code_filepath
        with open(input_filepath, 'r') as file:
            self.input_text = file.read()

        self.input_filepath = input_filepath
        # changing working directory to directory from which came file with source code
        working_directory = self.file_path[0:self.file_path.rfind('/')] + '/'
        os.chdir(working_directory)

    def compile_and_run(self):
        # compile
        self.compilation_logs = self.compile()

        # execute program only, if compilation was successful
        if self.compilation_logs == "":
            self.output_file_name = self.input_filepath[self.input_filepath.rfind('/')+1:self.input_filepath.rfind('.')] + ".out"
            # run with given input and test execution time
            start = datetime.datetime.now() # start timer
            res = subprocess.run(['./a.out'], capture_output=True, text=True, input=self.input_text, check=True)
            os.remove("a.out")
            self.output_text = res.stdout
            end = datetime.datetime.now() # end timer
            self.execution_time = int((end-start).total_seconds() * 1000)

    # function also returns name of .out file
    def save_output_to_file(self):
        # .out name will be named as .in file
        # e.g. output for file test1.in will be saved as test1.out file
        try:
            #create .out file
            output_file = open(self.output_file_name, 'w+')
            output_file.write(self.output_text)
        except Exception as e:
            raise e

    def compile(self):
        res = subprocess.run(['g++', self.file_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return res.stdout.decode('utf-8')

    def getLeaksLogs(self):
        # program needs to be compiled
       command = 'leaks -atExit -- ./a.out <' + str(self.input_filepath) + '| grep LEAK'
       res = subprocess.run(command, text=True, capture_output=True, shell=True)
       os.remove("a.out")
       return res.stdout

    def check_leaks(self):
        # compile
        self.compilation_logs = self.compile()
        # check for leaks only, if compilation was successful
        if self.compilation_logs == "":
            self.leaks_logs = self.getLeaksLogs()

    # execution time in ms
    def get_execution_time(self) -> int:
        return self.execution_time

    def get_output(self) -> str:
        return self.output_text

    # if function return nothing, compilation was successful
    def get_compilation_logs(self) -> str:
        return self.compilation_logs

    def get_leaks_logs(self):
        return self.leaks_logs

    def get_output_file_name(self):
        return self.output_file_name