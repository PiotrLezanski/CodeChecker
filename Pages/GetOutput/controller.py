
from tkinter import filedialog
import customtkinter as ctk
import tkinter
import subprocess
from CppExecution.CppFactory import CppFactory
from Tools.FileSingleton import FileSingleton

class Controller:
    def __init__(self, view):
        self.code_file_name = None
        self.input_file_name = None
        self.input_text = None
        self.input_file = None
        self.input_filepath = None
        self.code_filepath = None
        self.cppobject = None
        self.view = view
        self.singleton = FileSingleton.get_instance()

    def open_source_file(self):
        self.code_filepath = filedialog.askopenfilename(title="Choose a source file", initialdir="/", filetypes=[("Cpp files", "*.cpp")])
        self.code_file_name = self.code_filepath[self.code_filepath.rfind('/')+1:]
        # get working path
        if self.code_filepath != "":
            self.view.imported_file_name.configure(text=self.code_file_name)
            self.singleton.set_file(self.code_filepath)

    def open_input_file(self):
        self.input_filepath = filedialog.askopenfilename(title="Choose a input file", initialdir="/", filetypes=[(".txt", "*.txt"), (".in", "*.in")])
        if self.input_filepath != "":
            # get input to variable
            self.input_file = open(self.input_filepath, 'r')
            self.input_text = self.input_file.read()

            self.view.infile_preview.delete("0.0", tkinter.END) # clear textbox
            self.view.infile_preview.insert(tkinter.END, self.input_text) # add content of file

    def run_code(self):
        self.input_text = self.view.infile_preview.get("1.0", tkinter.END) # get input from textbox, if it was changed from file
        factory = CppFactory()
        if self.input_filepath is not None:
            f = open(self.input_filepath, 'w')
            f.write(self.input_text)
            f.close()
            # create CppObject
            self.cppobject = factory.create_cpp_object_from_filepath(0, self.input_filepath)
        else:
            self.cppobject = factory.create_cpp_object_from_text(0, self.input_text)

        self.cppobject.compile_and_run()
        # if compilation was successful
        if self.cppobject.get_compilation_logs() == "":
            # if run button pushed, generate .out file and its preview
            self.view.generate_output_frame(self.cppobject)
        else:
            self.view.infile_preview.delete("0.0", tkinter.END)
            self.view.infile_preview.insert("0.0", "Compilation error:\n" + self.cppobject.get_compilation_logs())

    def open_preview_window(self):
        if self.view.toplevel_window is None or not self.view.toplevel_window.winfo_exists():
            self.view.toplevel_window = ctk.CTkToplevel(self.view)  # create window if its None or destroyed
            self.view.toplevel_window.rowconfigure(0, weight=1)
            self.view.toplevel_window.columnconfigure(0, weight=1)
            self.view.toplevel_window.title("output file preview")
            self.view.toplevel_window.geometry("310x370")
            self.view.output_preview = ctk.CTkTextbox(self.view.toplevel_window)
            self.view.output_preview.grid(row=0, column=0, sticky="nesw")

            self.view.output_preview.delete("0.0", tkinter.END)
            self.view.output_preview.insert("0.0", self.cppobject.get_output())
        else:
            self.view.toplevel_window.focus()  # if window exists focus it

    def update_code(self, i):
        self.view.imported_file_name.configure(text=self.singleton.get_filename())