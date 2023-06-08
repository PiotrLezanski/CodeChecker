import customtkinter as ctk
from tkinter import messagebox, filedialog
from Tools.FileSingleton import *
from Tools.TestCase import *
from CppExecution.CppFactory import CppFactory, CppObject

class Controller:
    def __init__(self, view):
        self.generated_output = None
        self.code_filepath = None
        self.output_texts = None
        self.code_filename = None
        self.path = None
        self.view = view
        self.singleton = FileSingleton.get_instance()

    def open_source_file(self):
        self.code_filepath = filedialog.askopenfilename(title="Choose a source file", initialdir="/", filetypes=[("Cpp files", "*.cpp")])
        if self.code_filepath != "":
            self.view.import_source_button._bg_color = "green"
            self.code_filename = self.code_filepath[self.code_filepath.rfind('/')+1:]
            self.view.file_name.configure(text=self.code_filename)
            self.singleton.set_file(self.code_filepath)

    def load_tests(self):
        if self.view.number_of_tests is not None:
            self.view.hide_testcases()
        self.view.number_of_tests = self.view.test_number_entry.get()

        if self.view.number_of_tests.isnumeric() == False or not 0 < int(self.view.number_of_tests) <= 10:
            messagebox.showerror("Error message", "Please enter valid number of testcases")
            self.view.number_of_tests = None

        self.view.create_testcase_components()
        curr_row = 3
        for i in range(int(self.view.number_of_tests)):
            self.view.generate_testcase_frame(i, curr_row)
            curr_row = curr_row + 3

    def create_testcase(self, i):
        # self.testcases_list = [None] * int(self.view.number_of_tests)
        test_case = TestCase(0, self.view.input_texts[i].get("0.0", "end"), self.view.output_texts[i].get("0.0", "end"))
        if test_case.get_compilation_logs() != "":
            # compilation unsuccessful
            self.generated_output = "Compilation error:\n" + str(test_case.get_compilation_logs())
            self.view.run_test_buttons[i]._bg_color = "blue"
        else:
            # compilation successful, now compare outputs
            if test_case.compare_output():
                self.generated_output = "PASSED"
                self.view.run_test_buttons[i]._bg_color = "green"
            else:
                self.generated_output = "WRONG"
                self.view.run_test_buttons[i]._bg_color = "red"

    def run_testcase(self, i):
        if self.view.input_texts[i] is not None and self.view.output_texts[i] is not None:
            self.create_testcase(i)
            self.view.output_texts[i].delete("0.0", "end")
            self.view.output_texts[i].insert("0.0", str(self.generated_output))

    def update_code(self, i):
        self.view.file_name.configure(text=self.singleton.get_filename())

# TODO: - run all button, - exceptions (e.x. file not given)