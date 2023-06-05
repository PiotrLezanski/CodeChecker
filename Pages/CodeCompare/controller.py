import tkinter
from tkinter import filedialog

import customtkinter as ctk
from Tools.FileSingleton import FileSingleton

from Tools.EfficiencyChecker import EfficiencyChecker


class Controller:
    def __init__(self, view):
        self.view = view
        self.checker = EfficiencyChecker()

    def load_source_file(self, file_number):
        path = filedialog.askopenfilename(title="Choose a source file", initialdir="/",
                                          filetypes=[("Cpp files", "*.cpp")])
        # get working path
        if path != "":
            self.view.import_first_source_button._bg_color = "green"
            components = path.split("/")
            file_name = components[len(components) - 1]
            if file_number == 1:
                self.view.first_file_name.configure(text=file_name)
                FileSingleton.set_file(path, 0)
            elif file_number == 2:
                self.view.second_file_name.configure(text=file_name)
                FileSingleton.set_file(path, 1)

    def run(self):
        pass