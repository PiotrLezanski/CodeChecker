import customtkinter as ctk
from tkinter import filedialog
from Tools.FileSingleton import FileSingleton


class Controller:
    def __init__(self, view):
        self.view = view
        self.singleton = FileSingleton.get_instance()

    def load_file(self, text_box, _id):
        filepath = filedialog.askopenfilename(title="Choose a code file",
                                              initialdir="/",
                                              filetypes=[(".cpp", "*.cpp")])
        if _id == 1:
            self.singleton.set_file1(filepath)
            text_box.insert("0.0", self.singleton.get_file1_text())
        elif _id == 2:
            self.singleton.set_file2(filepath)
            text_box.insert("0.0", self.singleton.get_file2_text())
