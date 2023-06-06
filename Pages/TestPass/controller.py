import customtkinter as ctk
from tkinter import messagebox

class Controller:
    def __init__(self, view):
        self.view = view

    def open_source_file(self):
        return

    def load_tests(self):
        if self.view.number_of_tests is not None:
            self.view.hide_testcases()
        self.view.number_of_tests = self.view.test_number_entry.get()

        if self.view.number_of_tests.isnumeric() == False or not 0 < int(self.view.number_of_tests) <= 10:
            messagebox.showerror("Error message", "Please enter valid number of testcases")
            self.view.number_of_tests = None

        self.view.create_testcase_components()
        curr_row = 2
        for i in range(int(self.view.number_of_tests)):
            self.view.generate_testcase_frame(i, curr_row)
            curr_row = curr_row + 3

    def run_testcase(self, i):
        pass
