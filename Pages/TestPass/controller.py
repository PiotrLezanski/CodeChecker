import customtkinter as ctk

class Controller:
    def __init__(self, view):
        self.view = view

    def open_source_file(self):
        return

    def load_tests(self):
        # self.view.generate_testcase_frame(2)
        self.view.number_of_tests = self.view.test_number_entry.get()
        self.view.create_testcase_components()
        curr_row = 2
        for i in range(int(self.view.number_of_tests)):
            self.view.generate_testcase_frame(i, curr_row)
            curr_row = curr_row + 3