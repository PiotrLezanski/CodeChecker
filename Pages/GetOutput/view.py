from Pages.GetOutput.controller import Controller
from Tools.FileSingleton import FileSingleton
import customtkinter as ctk

class View(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = Controller(self)

        # output frame
        self.output_label = None
        self.output_frame = None
        self.save_output_button = None
        self.preview_button = None
        self.toplevel_window = None

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

        self.import_source_button = ctk.CTkButton(self.code_frame, text="Choose file", fg_color="transparent", border_width=2, command=self.controller.open_source_file)
        self.import_source_button.grid(row=1, column=2, padx=10, pady=10, sticky="nw")

        # get imported file name
        if FileSingleton.get_filepath(0) is None:
            text = "No file uploaded"
        else:
            self.import_source_button._bg_color = "green"
            text = FileSingleton.get_filepath(0)[FileSingleton.get_filepath(0).rfind('/'):]
        self.imported_file_name = ctk.CTkLabel(self.code_frame, text=text)
        self.imported_file_name.grid(row=1, column=3)

        # .in file and run button
        self.infile_frame  = ctk.CTkFrame(self)
        self.infile_frame.grid(row=1, column=1, padx=20, pady=10, sticky="ew")
        self.infile_label = ctk.CTkLabel(self.infile_frame, text="Import file with input or modify textbox")
        self.infile_label.grid(row=1, column=1, padx=20, pady=10)
        self.infile_button = ctk.CTkButton(self.infile_frame, text="Choose file", fg_color="transparent", border_width=2, command=self.controller.open_input_file)
        self.infile_button.grid(row=1, column=2, padx=20, pady=10)
        self.run_button = ctk.CTkButton(self.infile_frame, text="RUN", width=100, command=self.controller.run_code)
        self.run_button.grid(row=1, column=3, padx=10, pady=10)
        # input file preview
        self.infile_preview = ctk.CTkTextbox(self, height=200)
        self.infile_preview.grid(row=2, column=1, padx=20, pady=10, sticky="new")

    def generate_output_frame(self, cppobject):
        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.grid(row=3, column=1, columnspan=3, padx=20, pady=10, sticky="nesw")
        try:
            self.output_label = ctk.CTkLabel(self.output_frame, text="Output: " + cppobject.get_output_file_name())
        except:
            self.output_label = ctk.CTkLabel(self.output_frame, text="Output: test.out")
        self.output_label.grid(row=3, column=1, padx=10, pady=20)
        self.output_frame.rowconfigure(3, weight=1)

        self.toplevel_window = None
        self.preview_button = ctk.CTkButton(self.output_frame, text="Preview", fg_color="transparent",
                                                 border_width=2, command=self.controller.open_preview_window)
        self.preview_button.grid(row=3, column=2, padx=10)

        self.save_output_button = ctk.CTkButton(self.output_frame, text="Save .out file",
                                                     command=cppobject.save_output_to_file)
        self.save_output_button.grid(row=3, column=3, padx=10)