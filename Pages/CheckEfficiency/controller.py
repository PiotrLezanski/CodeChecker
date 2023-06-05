import tkinter
from tkinter import filedialog
from Tools.EfficiencyChecker import EfficiencyChecker
import customtkinter as ctk

from Tools.FileSingleton import FileSingleton


class Controller:
    def __init__(self, view):
        self.path = None
        self.input_file = None
        self.input_text = None
        self.checker = None
        self.view = view

    def load_source_file(self):
        path = filedialog.askopenfilename(title="Choose a source file", initialdir="/",
                                          filetypes=[("Cpp files", "*.cpp")])
        # get working path
        if path != "":
            self.view.import_source_button._bg_color = "green"  # change color when imported
            components = path.split("/")
            file_name = components[len(components) - 1]
            self.view.file_name.configure(text=file_name)

            FileSingleton.set_file(path)

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
        # no files uploaded
        if FileSingleton.get_file(0) is None and FileSingleton.get_file(1) is None:
            return

        # no testcase
        if self.input_text is None:
            return

        self.checker = EfficiencyChecker(self.path)

        time = self.checker.check_time() if self.view.checkbox_vars[0].get() == 1 else "Not checked"
        leaks = self.checker.check_leaks() if self.view.checkbox_vars[1].get() == 1 else "Not checked"
        logs = self.checker.check_logs() if self.view.checkbox_vars[2].get() == 1 else "Not checked"

        self.generate_popup_window(time, leaks, logs)

    def generate_popup_window(self, time, leaks, logs):
        # if popup does not exist create new one else focus on it
        if self.view.toplevel_window is None or not self.view.toplevel_window.winfo_exists():
            self.view.toplevel_window = ctk.CTkToplevel(self.view)
            self.view.toplevel_window.title("Results")
            self.view.toplevel_window.geometry("510x400")
            self.view.toplevel_window.rowconfigure(0, weight=1)
            self.view.toplevel_window.columnconfigure(0, weight=1)
            self.view.result_preview = ctk.CTkTextbox(self.view.toplevel_window, width=200, height=200, disabled=True)
            self.view.result_preview.grid(row=0, column=0, sticky="nsew")
            self.view.result_preview.delete("0.0", tkinter.END)  # clear textbox
            text = "Time: " + time + "\nLeaks: " + leaks + "\nLogs: " + logs
            self.view.result_preview.insert(tkinter.END, text)  # add content of file
        else:
            self.view.toplevel_window.focus()