import customtkinter as ctk
from tkinter import filedialog
from Tools.FileSingleton import FileSingleton


class Controller:
    def __init__(self, view):
        self.view = view
        self.singleton = FileSingleton.get_instance()

    def load_file(self, _id, label, text_box):
        filepath = filedialog.askopenfilename(title="Choose a code file",
                                              initialdir="/",
                                              filetypes=[(".cpp", "*.cpp")])
        file_name = None
        file_code = None
        if _id == 1:
            self.singleton.set_file1(filepath)
            file_name = 1
            file_code = self.singleton.get_file1_text()
        elif _id == 2:
            self.singleton.set_file2(filepath)
            file_name = 2
            file_code = self.singleton.get_file2_text()
        label.configure(text=file_name)
        text_box.insert("0.0", file_code)

    def update_checkboxes(self, recently_used):
        for checkbox in self.view.checkboxes:
            checkbox.deselect()
        recently_used.select()
        chosen = self.view.checkboxes.index(recently_used)
        self.singleton.set_default(chosen)
