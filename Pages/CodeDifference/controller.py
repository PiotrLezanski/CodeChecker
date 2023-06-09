from tkinter import filedialog
from Tools.FileSingleton import FileSingleton
from difflib import Differ


class Controller:
    def __init__(self, view):
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
                self.view.first_file_name.configure(text=file_name)
                self.singleton.set_file(path, 0)
            elif file_number == 1:
                self.view.second_file_name.configure(text=file_name)
                self.singleton.set_file(path, 1)

    def run(self):
        if self.singleton.get_file(0) is None or self.singleton.get_file(1) is None:
            return

        differ = Differ()

        text = ""

        self.singleton.reset_reading_position(0)
        self.singleton.reset_reading_position(1)

        for line in differ.compare(self.singleton.get_file(0).readlines(), self.singleton.get_file(1).readlines()):
            if line.startswith("-"):
                text += "File 1 has: " + line[2:]
            elif line.startswith("+"):
                text += "File 2 has: " + line[2:]
        if text == "":
            text = "Files are identical"

        self.view.generate_output_frame(text)

        self.singleton.reset_reading_position(0)
        self.singleton.reset_reading_position(1)

    def update_code(self, i):
        self.view.first_file_name.configure(text=self.singleton.get_filename(0))
        self.view.second_file_name.configure(text=self.singleton.get_filename(1))