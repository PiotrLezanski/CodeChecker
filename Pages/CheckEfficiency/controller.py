import tkinter
from tkinter import filedialog, messagebox
import customtkinter as ctk

from Tools.FileSingleton import FileSingleton

from Tools.EfficiencyChecker import EfficiencyChecker
import Tools


class Controller:
    def __init__(self, view):
        self.path = None
        self.input_file = None
        self.input_text = None
        self.checker = None
        self.view = view
        self.__instance = FileSingleton.get_instance()

    def load_source_file(self):
        path = filedialog.askopenfilename(title="Choose a source file", initialdir="/",
                                          filetypes=[("Cpp files", "*.cpp")])
        # get working path
        if path != "":
            self.__instance.set_file(path)
            self.view.file_name.configure(text=self.__instance.get_filename())

    def open_testcase_file(self):
        self.path = filedialog.askopenfilename(title="Choose a input file", initialdir="/",
                                               filetypes=[("Text files", "*.txt"), ("In files", "*.in")])
        if self.path != "":
            self.input_file = open(self.path, 'r')
            self.input_text = self.input_file.read()
            self.input_file.close()
            self.view.infile_preview.delete("0.0", tkinter.END)  # clear textbox
            self.view.infile_preview.insert(tkinter.END, self.input_text)  # add content of file

    def run(self):
        # no default file uploaded
        if self.__instance.get_file() is None:
            messagebox.showerror("Error message", "No source file attached")
            return

        if self.view.checkbox_vars[0].get() == 0 and self.view.checkbox_vars[1].get() == 0 and self.view.checkbox_vars[
            2].get() == 0:
            messagebox.showerror("Error message", "Choose at least 1 checkbox")
            return

        self.input_text = self.view.infile_preview.get("1.0", tkinter.END)

        self.checker = Tools.EfficiencyChecker.EfficiencyChecker(self.__instance.get_default(), self.input_text)

        logs = self.checker.check_logs()
        if logs == "Compilation successful":
            time = self.checker.check_time() if self.view.checkbox_vars[0].get() == 1 else "Not checked"
            leaks = self.checker.check_leaks() if self.view.checkbox_vars[1].get() == 1 else "Not checked"
            logs_information = logs if self.view.checkbox_vars[2].get() == 1 else "Not checked"
            text = "Logs: " + str(logs_information) + "\n\nTime: " + str(time) + "\n\nLeaks: " + str(leaks) + "\n\n"
        else:
            text = "Logs: " + str(logs) + "\n\n"

        self.view.generate_output_frame(text)

    def update_code(self, i):
        name = self.__instance.get_filename()
        if name != "":
            self.view.file_name.configure(text=self.__instance.get_filename())
        else:
            self.view.file_name.configure(text="No file")
