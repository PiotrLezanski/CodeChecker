import tkinter
from tkinter import messagebox
from tkinter import filedialog
import customtkinter as ctk

import subprocess

# from CppExecution import CppFactory
# from CppExecution import CppObject

# from CppExecution.CppFactory import CppFactory
# from CppExecution.CppObject import CppObject

from Tools import FileSingleton

class Controller():
    def __init__(self, view):
        self.view = view

    def open_source_file(self):
        self.code_filepath = filedialog.askopenfilename(title="Choose a source file", initialdir="/", filetypes=[("Cpp files", "*.cpp")])
        # get working path
        if self.code_filepath != "":
            # get code to variable
            source_file = open(self.code_filepath, 'r')
            self.code_text = source_file.read()

            self.view.import_source_button._bg_color = "green" # change color when imported
            components = self.code_filepath.split("/")
            self.source_code_file_name = components[len(components)-1]

            self.view.imported_file_name = ctk.CTkLabel(self.view.code_frame, text=self.source_code_file_name)
            self.view.imported_file_name.grid(row=1, column=3)
            source_file.close()

    def open_input_file(self):
        self.input_filepath = filedialog.askopenfilename(title="Choose a input file", initialdir="/", filetypes=[(".txt", ".in")])
        if self.input_filepath != "":
            # get input to variable
            self.input_file = open(self.input_filepath, 'r')
            self.input_text = self.input_file.read()

            self.view.infile_button._bg_color = "green" # change color when imported
            components = self.input_filepath.split("/")
            self.input_file_name = components[len(components)-1]
            
            self.view.infile_preview.delete("0.0", tkinter.END) # clear textbox
            self.view.infile_preview.insert(tkinter.END, self.input_text) # add content of file

    def run_code(self):
        # insert input from textbox to file
        self.input_text = self.view.infile_preview.get("1.0", tkinter.END) # get input from textbox, if it was changed from file
        f = open(self.input_filepath, 'w')
        f.write(self.input_text)
        f.close()

        # create CppFactory and CppObject
        factory = CppFactory(10000)
        try:
            cppobject = CppFactory.CppObjectFromFilepath(self.code_filepath, self.input_filepath)
        except:
            messagebox.showerror("showerror", "You need to add source file and provide input")

        # if compilation was successful
        if cppobject.get_compilation_logs() == "":
            # if run button pushed, generate .out file and its preview
            self.view.output_frame = ctk.CTkFrame(self)
            self.view.output_frame.grid(row=3, column=1, columnspan=3, padx=20, pady=10, sticky="nesw")
            try:
                self.view.output_label = ctk.CTkLabel(self.output_frame, text="Output: " + cppobject.output_file_name())
            except:
                self.view.output_label = ctk.CTkLabel(self.output_frame, text="Output: test.out")
            self.view.output_label.grid(row=3, column=1, padx=10, pady=20)
            self.view.output_frame.rowconfigure(3,weight=1)

            self.toplevel_window = None 
            self.view.preview_button = ctk.CTkButton(self.output_frame, text="Preview", fg_color="transparent", border_width=2, command=self.open_preview_window)
            self.view.preview_button.grid(row=3, column=2, padx=10)

            self.view.save_output_button = ctk.CTkButton(self.output_frame, text="Save .out file", command=self.save_output_file)
            self.view.save_output_button.grid(row=3, column=3, padx=10)
            
    def open_preview_window(self):
        if self.view.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.view.toplevel_window = ctk.CTkToplevel(self)  # create window if its None or destroyed
            self.view.toplevel_window.rowconfigure(0, weight=1)
            self.view.toplevel_window.columnconfigure(0, weight=1)
            self.view.toplevel_window.title("output file preview")
            self.view.toplevel_window.geometry("310x370")
            self.view.output_preview = ctk.CTkTextbox(self.toplevel_window)
            self.view.output_preview.grid(row=0, column=0, sticky="nesw")

            self.view.output_preview.delete("0.0", tkinter.END)
            self.view.output_preview.insert("0.0", self.result.stdout)
        else:
            self.view.toplevel_window.focus()  # if window exists focus it