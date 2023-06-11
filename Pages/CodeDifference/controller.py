import sys
from tkinter import filedialog
from Tools.FileSingleton import FileSingleton
from difflib import Differ, unified_diff
from Tools.PopUpWindow import generate_popup_window


class Controller:
    def __init__(self, view):
        self.view = view
        self.singleton = FileSingleton.get_instance()

    def load_source_file(self, file_number):
        path = filedialog.askopenfilename(title="Choose a source file", initialdir="/",
                                          filetypes=[("Cpp files", "*.cpp")])
        # get working path
        if path != "":
            components = path.split("/")
            file_name = components[len(components) - 1]
            if file_number == 0:
                self.view.first_file_name.configure(text=file_name)
                self.singleton.set_file(path, 0)
            elif file_number == 1:
                self.view.second_file_name.configure(text=file_name)
                self.singleton.set_file(path, 1)

    def run(self):
        if self.singleton.get_file(0) is None or self.singleton.get_file(1) is None:
            generate_popup_window("No files attached", self.view)
            return

        differ = Differ()

        text = ""

        self.singleton.reset_reading_position(0)
        self.singleton.reset_reading_position(1)

        diff_lines = []
        file1 = self.singleton.get_file(0).readlines()
        file2 = self.singleton.get_file(1).readlines()

        difference = (unified_diff(file1, file2, fromfile=self.singleton.get_filepath(0),
                                   tofile=self.singleton.get_filepath(1), lineterm=''))
        for line in difference:
            text += line + "\n"

        if text == "":
            text = "Files are identical"

        self.view.generate_output_frame(text)

        self.singleton.reset_reading_position(0)
        self.singleton.reset_reading_position(1)

    def update_code(self, i):
        if self.singleton.get_filename(0) != "":
            self.view.first_file_name.configure(text=self.singleton.get_filename(0))
        if self.singleton.get_filename(1) != "":
            self.view.second_file_name.configure(text=self.singleton.get_filename(1))