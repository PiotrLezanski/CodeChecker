import tkinter
from tkinter import filedialog

import customtkinter as ctk
from Tools.FileSingleton import FileSingleton

from Tools.EfficiencyChecker import EfficiencyChecker


class Controller:
    def __init__(self, view):
        self.second_path = None
        self.first_path = None
        self.checker = [None, None]
        self.input_text = None
        self.input_file = None
        self.path = None
        self.view = view
        self.singleton = FileSingleton.get_instance()

    def load_source_file(self, file_number):
        path = filedialog.askopenfilename(title="Choose a source file", initialdir="/",
                                          filetypes=[("Cpp files", "*.cpp")])
        # get working path
        if path != "":
            if file_number == 0:
                self.view.import_first_source_button._bg_color = "green"
            else:
                self.view.import_second_source_button._bg_color = "green"
            components = path.split("/")
            file_name = components[len(components) - 1]

            if file_number == 0:
                self.first_path = path
            else:
                self.second_path = path;

            if file_number == 0:
                self.view.first_file_name.configure(text=file_name)
                self.singleton.set_file(path, 0)
            elif file_number == 1:
                self.view.second_file_name.configure(text=file_name)
                self.singleton.set_file(path, 1)

    def open_testcase_file(self):
        self.path = filedialog.askopenfilename(title="Choose a input file", initialdir="/",
                                               filetypes=[("Text files", "*.txt"), ("In files", "*.in")])
        if self.path != "":
            self.view.infile_button._bg_color = "green"  # change color when imported
            components = self.path.split("/")
            input_file_name = components[len(components) - 1]
            self.input_file = open(self.path, 'r')
            self.input_text = self.input_file.read()
            self.view.infile_preview.delete("0.0", tkinter.END)  # clear textbox
            self.view.infile_preview.insert(tkinter.END, self.input_text)  # add content of file

    def run(self):
        if self.singleton.get_file(0) is None or self.singleton.get_file(1) is None:
            return

        if self.input_text is None:
            return

        self.checker[0] = EfficiencyChecker(0, self.first_path)
        self.checker[1] = EfficiencyChecker(1, self.second_path)

        logs = ["", ""]
        logs[0] = self.checker[0].check_logs()
        logs[1] = self.checker[1].check_logs()

        text = ["", ""]

        if logs[0] == "Compilation successful" and logs[1] == "Compilation successful":
            time = ["", ""]
            if self.view.checkbox_vars[0].get() == 1:
                time[0] = self.checker[0].check_time()
                time[1] = self.checker[1].check_time()
            else:
                time[0] = "Not checked"
                time[1] = "Not checked"

            leaks = ["", ""]
            if self.view.checkbox_vars[1].get() == 1:
                leaks[0] = self.checker[0].check_leaks()
                leaks[1] = self.checker[1].check_leaks()
            else:
                leaks[0] = "Not checked"
                leaks[1] = "Not checked"

            if self.view.checkbox_vars[2].get() == 0:
                logs[0] = "Not checked"
                logs[1] = "Not checked"

            text[0] = "Logs: " + str(logs[0]) + "\n\nTime: " + str(time[0]) + "\n\nLeaks: " + str(leaks[0]) + "\n\n"
            text[1] = "Logs: " + str(logs[1]) + "\n\nTime: " + str(time[1]) + "\n\nLeaks: " + str(leaks[1]) + "\n\n"
        else:
            text[0] = "Logs: " + str(logs[0]) + "\n\n"
            text[1] = "Logs: " + str(logs[1]) + "\n\n"

        self.view.generate_output_frame(text)

    def update_code(self, i):
        self.view.first_file_name.configure(text=self.singleton.get_filename(0))
        self.view.second_file_name.configure(text=self.singleton.get_filename(1))
