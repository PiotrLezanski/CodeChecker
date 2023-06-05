import tkinter
import customtkinter as ctk
from Pages.GetOutput.controller import Controller


class View(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)

        # create controller
        controller = Controller(self)

        # language picker
        self.code_frame = ctk.CTkFrame(self)
        self.code_frame.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        self.language_picker_label = ctk.CTkLabel(self.code_frame, text="Pick programming language")
        self.language_picker_label.grid(row=0, column=1, padx=10, pady=10, sticky="nw")
        self.language_picker = ctk.CTkOptionMenu(self.code_frame, values=["C++"])
        self.language_picker.grid(row=0, column=2, padx=10, pady=10, sticky="nw")
        # source file
        self.import_source_label = ctk.CTkLabel(self.code_frame, text="Import source code")
        self.import_source_label.grid(row=1, column=1, padx=10, pady=10, sticky="nw")
        self.import_source_button = ctk.CTkButton(self.code_frame, text="Choose file", fg_color="transparent", border_width=2, command=controller.open_source_file)
        self.import_source_button.grid(row=1, column=2, padx=10, pady=10, sticky="nw")
        # .in file and run button
        self.infile_frame  = ctk.CTkFrame(self)
        self.infile_frame.grid(row=1, column=1, padx=20, pady=10, sticky="ew")
        self.infile_label = ctk.CTkLabel(self.infile_frame, text="Import file with input or modify textbox")
        self.infile_label.grid(row=1, column=1, padx=20, pady=10)
        self.infile_button = ctk.CTkButton(self.infile_frame, text="Choose file", fg_color="transparent", border_width=2, command=controller.open_input_file)
        self.infile_button.grid(row=1, column=2, padx=20, pady=10)
        self.run_button = ctk.CTkButton(self.infile_frame, text="RUN", width=100, command=controller.run_code)
        self.run_button.grid(row=1, column=3, padx=10, pady=10)
        # input file preview
        self.infile_preview = ctk.CTkTextbox(self, height=200)
        self.infile_preview.grid(row=2, column=1, padx=20, pady=10, sticky="new")