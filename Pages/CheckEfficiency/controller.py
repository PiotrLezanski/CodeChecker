from tkinter import filedialog
import customtkinter as ctk

from Tools import FileSingleton


class Controller:
    def __init__(self, view):
        self.view = view


    def load_source_file(self):
        if FileSingleton.FileSingleton.get_file1() is None:
            self.isLeft = True
        elif FileSingleton.FileSingleton.get_file1() is None and FileSingleton.FileSingleton.get_file2() is None:
            self.isLeft = True
        else:
            self.isLeft = False

        self.source_code = filedialog.askopenfilename(title="Choose a source file", initialdir="/",
                                                      filetypes=[("Cpp files", "*.cpp")])
        # get working path
        if self.source_code != "":
            self.view.import_source_button._bg_color = "green"  # change color when imported
            components = self.source_code.split("/")
            self.file_name = components[len(components) - 1]
            self.view.file_name.configure(text=self.file_name)

        if self.isLeft:
            FileSingleton.FileSingleton.set_file1(self.source_code)
        else:
            FileSingleton.FileSingleton.set_file2(self.source_code)
