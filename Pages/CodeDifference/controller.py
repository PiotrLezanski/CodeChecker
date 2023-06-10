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

        diff_lines = []
        file1 = self.singleton.get_file(0).readlines()
        file2 = self.singleton.get_file(1).readlines()
        max_lines = max(len(file1), len(file2))
        for line_num in range(max_lines):
            line1 = file1[line_num].strip() if line_num < len(file1) else ""
            line2 = file2[line_num].strip() if line_num < len(file2) else ""
            if line1 != line2:
                diff_lines.append((line_num + 1, line1, line2))

        if len(diff_lines) == 0:
            text = "Files are identical"
        else:
            for line_num, line1, line2 in diff_lines:
                text += "Difference at line " + str(line_num) + "\n"
                text += "File 1 has: " + line1 + "\n"
                text += "File 2 has: " + line2 + "\n"
                text += "\n"

        self.view.generate_output_frame(text)

        self.singleton.reset_reading_position(0)
        self.singleton.reset_reading_position(1)

    def update_code(self, i):
        if self.singleton.get_filename(0) != "":
            self.view.first_file_name.configure(text=self.singleton.get_filename(0))
        if self.singleton.get_filename(1) != "":
            self.view.second_file_name.configure(text=self.singleton.get_filename(1))