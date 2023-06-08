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
        test_case = TestCase(self.singleton.get_default(), self.view.input_texts[i].get("0.0", "end"), self.view.output_texts[i].get("0.0", "end"))
        if test_case.get_compilation_logs() != "":
            # compilation unsuccessful
            self.generated_output = f"Test {i+1}: Compilation error:\n" + str(test_case.get_compilation_logs())
            self.view.run_test_buttons[i]._bg_color = "blue"
        else:
            # compilation successful, now compare outputs
            if test_case.compare_output():
                self.generated_output = f"Test {i+1}: PASSED"
                self.view.run_test_buttons[i]._bg_color = "green"
            else:
                tmp = self.view.output_texts[i].get("0.0", "end")
                self.generated_output = f"\nTest {i+1}: NOT PASSED\nYour output:\n{tmp}\nExpected output:\n{test_case.get_output()}"
                self.view.run_test_buttons[i]._bg_color = "red"

    def run_testcase(self, i):
        if self.view.input_texts[i] is not None and self.view.output_texts[i] is not None and self.singleton.get_filepath() != "":
            self.create_testcase(i)
            self.view.output_texts[i].delete("0.0", "end")
            self.view.output_texts[i].insert("0.0", str(self.generated_output))
        else:
            messagebox.showerror("Error message", "You need to provide input, expected output and .cpp file")

    def run_all_testcases(self):
        result = ""
        for i in range(int(self.view.number_of_tests)):
            self.create_testcase(i)
            result = result + self.generated_output + '\n'

        self.open_preview_window(result)

    def open_preview_window(self, result):
        if self.view.toplevel_window is None or not self.view.toplevel_window.winfo_exists():
            self.view.toplevel_window = ctk.CTkToplevel(self.view)  # create window if its None or destroyed
            self.view.toplevel_window.rowconfigure(0, weight=1)
            self.view.toplevel_window.columnconfigure(0, weight=1)
            self.view.toplevel_window.title("output file preview")
            self.view.toplevel_window.geometry("310x370")
            self.view.output_preview = ctk.CTkTextbox(self.view.toplevel_window)
            self.view.output_preview.grid(row=0, column=0, sticky="nesw")

            self.view.output_preview.delete("0.0", "end")
            self.view.output_preview.insert("0.0", result)
        else:
            self.view.toplevel_window.focus()

    def update_code(self, i):
        self.view.file_name.configure(text=self.singleton.get_filename())

# TODO: - run all button, - exceptions (e.x. file not given)