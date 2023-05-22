import tkinter
from tkinter import filedialog
from tkinter import messagebox
import customtkinter as ctk
import subprocess
import os

class MainWindow(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)


    # configure grid layout
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)
        # self.grid_rowconfigure(0, weight=0)
        # self.grid_rowconfigure(1, weight=0)
        # self.grid_rowconfigure(3, weight=1)

    # main
        # language picker
        self.code_frame = ctk.CTkFrame(self)
        self.code_frame.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        self.language_picker_label = ctk.CTkLabel(self.code_frame, text="Pick programming language")
        self.language_picker_label.grid(row=0, column=1, padx=10, pady=10, sticky="nw")
        self.language_picker = ctk.CTkOptionMenu(self.code_frame, values=["C++", "Java"])
        self.language_picker.grid(row=0, column=2, padx=10, pady=10, sticky="nw")
        # source file
        self.import_source_label = ctk.CTkLabel(self.code_frame, text="Import source code")
        self.import_source_label.grid(row=1, column=1, padx=10, pady=10, sticky="nw")
        self.import_source_button = ctk.CTkButton(self.code_frame, text="Choose file", fg_color="transparent", border_width=2, command=self.open_source_file)
        self.import_source_button.grid(row=1, column=2, padx=10, pady=10, sticky="nw")
        # in file and run button
        self.infile_frame  = ctk.CTkFrame(self)
        self.infile_frame.grid(row=1, column=1, padx=20, pady=10, sticky="ew")
        self.infile_label = ctk.CTkLabel(self.infile_frame, text="Import file with input or modify textbox")
        self.infile_label.grid(row=1, column=1, padx=20, pady=10)
        self.infile_button = ctk.CTkButton(self.infile_frame, text="Choose file", fg_color="transparent", border_width=2, command=self.open_input_file)
        self.infile_button.grid(row=1, column=2, padx=20, pady=10)
        self.run_button = ctk.CTkButton(self.infile_frame, text="RUN", width=100, command=self.run_code)
        self.run_button.grid(row=1, column=3, padx=10, pady=10)
        # input file preview
        self.infile_preview = ctk.CTkTextbox(self, height=200)
        self.infile_preview.grid(row=2, column=1, padx=20, pady=10, sticky="new")

    def open_source_file(self):
        source_code = filedialog.askopenfilename(title="Choose a source file", initialdir="/", filetypes=[("Cpp files", "*.cpp")])
        # get working path
        if source_code != "":
            self.import_source_button._bg_color = "green" # change color when imported
            components = source_code.split("/")
            self.source_code_file_name = components[len(components)-1]
            self.imported_file_name = ctk.CTkLabel(self.code_frame, text=self.source_code_file_name)
            self.imported_file_name.grid(row=1, column=3)
            self.path = ""
            for i in range(0, len(components)-1):
                self.path += components[i] + "/"
            source_code = open(source_code, 'r')
            self.code = source_code.read()
        source_code.close()

    def open_input_file(self):
        input_file = filedialog.askopenfilename(title="Choose a input file", initialdir="/", filetypes=[(".txt", ".in")])
        if input_file != "":
            self.infile_button._bg_color = "green" # change color when imported
            components = input_file.split("/")
            self.input_file_name = components[len(components)-1]
            self.input_file = open(input_file, 'r')
            self.input_text = self.input_file.read()
            self.infile_preview.delete("0.0", tkinter.END) # clear textbox
            self.infile_preview.insert(tkinter.END, self.input_text) # add content of file

    def run_code(self):
        try:
            # compile c++ and send input 
            output_file = open('output.txt', 'w+')
            os.chdir(self.path) # change working category
            subprocess.run(['g++', '-o', 'CodeChecker', self.source_code_file_name])
            self.input_text = self.infile_preview.get("1.0", tkinter.END) # get input from textbox, if it was changed from file
            self.result = subprocess.run(['./CodeChecker'], capture_output=True, text=True, input=self.input_text, check=True)
            
            # if run button pushed, generate .out file and its preview
            # output
            self.output_frame = ctk.CTkFrame(self)
            self.output_frame.grid(row=3, column=1, columnspan=3, padx=20, pady=10, sticky="nesw")
            try:
                self.output_label = ctk.CTkLabel(self.output_frame, text="Output: " + self.input_file_name[0:self.input_file_name.find(".")] + ".out")
            except:
                self.output_label = ctk.CTkLabel(self.output_frame, text="Output: test.out")
            self.output_label.grid(row=3, column=1, padx=10, pady=20)
            self.output_frame.rowconfigure(3,weight=1)
            self.toplevel_window = None
            self.preview_button = ctk.CTkButton(self.output_frame, text="Preview", fg_color="transparent", border_width=2, command=self.open_preview_window)
            self.preview_button.grid(row=3, column=2, padx=10)
            self.save_output_button = ctk.CTkButton(self.output_frame, text="Save .out file", command=self.save_output_file)
            self.save_output_button.grid(row=3, column=3, padx=10)
        except: 
            # error
            messagebox.showerror("showerror", "You need to add source file and provide input")

    def open_preview_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ctk.CTkToplevel(self)  # create window if its None or destroyed
            self.toplevel_window.rowconfigure(0, weight=1)
            self.toplevel_window.columnconfigure(0, weight=1)
            self.toplevel_window.title("output file preview")
            self.toplevel_window.geometry("310x370")
            self.output_preview = ctk.CTkTextbox(self.toplevel_window)
            self.output_preview.grid(row=0, column=0, sticky="nesw")

            self.output_preview.delete("0.0", tkinter.END)
            self.output_preview.insert("0.0", self.result.stdout)
        else:
            self.toplevel_window.focus()  # if window exists focus it
        
    def save_output_file(self):
        try:
            out_file = open(self.input_file_name[0:self.input_file_name.find(".")] + ".out", 'w')
        except:
            out_file = open('test.out', 'w')
        out_file.write(self.result.stdout)
        out_file.close()
        self.save_output_button.configure(text="saved", fg_color="transparent")

