from Pages.CheckEfficiency.controller import Controller
from Tools import FileSingleton
import customtkinter as ctk
import tkinter


class View(ctk.CTkFrame):
    def __init__(self, parent, controller, singleton=FileSingleton.FileSingleton.get_instance()):
        ctk.CTkFrame.__init__(self, parent)

        self.controller = Controller(self)

        # input file container
        self.generate_file_container()

        # checkbox container
        self.generate_checkbox_row()

        # testcase container
        self.generate_testcase_container()

    def generate_file_container(self):
        self.import_file_frame = ctk.CTkFrame(self)
        self.import_file_frame.columnconfigure(0, weight=1)
        self.import_file_frame.columnconfigure(1, weight=1)
        self.import_file_frame.columnconfigure(2, weight=1)
        self.import_file_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.import_source_label = ctk.CTkLabel(self.import_file_frame, text="Import source code")
        self.import_source_label.grid(row=0, column=0, padx=10, pady=10)
        self.import_source_button = ctk.CTkButton(self.import_file_frame, text="Choose file", fg_color="transparent",
                                                  border_width=2, command=self.controller.load_source_file)
        self.import_source_button.grid(row=0, column=1, padx=10, pady=10)

        self.generate_file_name()


    def generate_file_name(self, singleton=FileSingleton.FileSingleton.get_instance()):
        # get file name
        if str(singleton.get_filepath1()) is None and str(singleton.get_filepath2()) is None:
            info_about_uploaded_files = "No files uploaded"
        elif str(singleton.get_filepath1()) is None:
            info_about_uploaded_files = str(singleton.get_filepath2())
        else:
            info_about_uploaded_files = str(singleton.get_filepath1())

        # display file name
        self.file_name = ctk.CTkLabel(self.import_file_frame, text=info_about_uploaded_files)
        self.file_name.grid(row=0, column=2, padx=10, pady=10)

    def generate_checkbox_row(self):

        # check time checkbox
        self.generate_checkbox(0, "Time")

        # check leaks checkbox
        self.generate_checkbox(1, "Leaks")

        # check logs checkbox
        self.generate_checkbox(2, "Logs")

    def generate_checkbox(self, checkbox_column, checkbox_text):
        # generate single checkbox in checkbox row
        self.check_time_checkbox = ctk.CTkCheckBox(self.import_file_frame, text=checkbox_text, border_width=2)
        self.check_time_checkbox.grid(row=1, column=checkbox_column, padx=10, pady=10)

    def generate_testcase_container(self):
        # frame for testcase
        self.infile_frame = ctk.CTkFrame(self)
        self.infile_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.infile_label = ctk.CTkLabel(self.infile_frame, text="Import file with input or modify textbox")
        self.infile_label.grid(row=1, column=0, padx=20, pady=10)
        self.infile_button = ctk.CTkButton(self.infile_frame, text="Choose file", fg_color="transparent",
                                           border_width=2)
        self.infile_button.grid(row=1, column=1, padx=20, pady=10)
        self.run_button = ctk.CTkButton(self.infile_frame, text="RUN", width=100)
        self.run_button.grid(row=1, column=2, padx=10, pady=10)
        # input file preview
        self.infile_preview = ctk.CTkTextbox(self, height=200)
        self.infile_preview.grid(row=2, column=0, padx=20, pady=10, sticky="new")





