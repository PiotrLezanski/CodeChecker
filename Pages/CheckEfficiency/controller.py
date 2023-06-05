import tkinter
from tkinter import filedialog
from Tools import EfficiencyChecker
import customtkinter as ctk

from Tools import FileSingleton


class Controller:
    def __init__(self, view):
        self.view = view
        self.checker = EfficiencyChecker.EfficiencyChecker()

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

    def open_testcase_file(self):
        input_file = filedialog.askopenfilename(title="Choose a input file", initialdir="/",
                                                filetypes=[(".txt", ".in")])
        if input_file != "":
            self.infile_button._bg_color = "green"  # change color when imported
            components = input_file.split("/")
            self.input_file_name = components[len(components) - 1]
            self.input_file = open(input_file, 'r')
            self.input_text = self.input_file.read()
            self.view.infile_preview.delete("0.0", tkinter.END)  # clear textbox
            self.view.infile_preview.insert(tkinter.END, self.input_text)  # add content of file

    def run(self):
        # no files uploaded
        if FileSingleton.FileSingleton.get_file(0) is None and FileSingleton.FileSingleton.get_file2() is None:
            return

        # no testcase
        if self.input_text == "":
            return

        self.time = self.checker.check_time() if self.view.checkbox_vars[0].get() == 1 else "Not checked"
        self.leaks = self.checker.check_leaks() if self.view.checkbox_vars[1].get() == 1 else "Not checked"
        self.logs = self.checker.check_logs() if self.view.checkbox_vars[2].get() == 1 else "Not checked"

        self.generate_popup_window()


    def generate_popup_window(self):
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
            self.text = "Time: " + self.time + "\nLeaks: " + self.leaks + "\nLogs: " + self.logs
            self.view.result_preview.insert(tkinter.END, self.text)  # add content of file
        else:
            self.view.toplevel_window.focus()


