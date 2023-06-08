from Pages.CheckEfficiency.controller import Controller
from Tools.FileSingleton import FileSingleton
import customtkinter as ctk
import tkinter


class View(ctk.CTkFrame):
    def __init__(self, parent, singleton=FileSingleton.get_instance()):
        ctk.CTkFrame.__init__(self, parent)

        self.output_preview = None
        self.output_button = None
        self.toplevel_window = None
        self.output_frame = None
        self.checkbox = None
        self.run_button = None
        self.infile_preview = None
        self.infile_label = None
        self.infile_button = None
        self.infile_frame = None
        self.check_time_checkbox = None
        self.checkbox_vars = None
        self.file_name = None
        self.import_source_button = None
        self.import_source_label = None
        self.import_file_frame = None
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

    def generate_file_name(self, singleton=FileSingleton.get_instance()):
        # get file name
        if singleton.get_filepath(0) is "" and singleton.get_filepath(1) is "":
            info_about_uploaded_files = "No file"
        elif singleton.get_filepath(0) is None:
            info_about_uploaded_files = str(singleton.get_filepath(1))
        else:
            info_about_uploaded_files = str(singleton.get_filepath(0))

        # display file name
        self.file_name = ctk.CTkLabel(self.import_file_frame, text=info_about_uploaded_files)
        self.file_name.grid(row=0, column=2, padx=10, pady=10)

    def generate_checkbox_row(self):

        self.checkbox_vars = [tkinter.IntVar() for _ in range(3)]
        # check time checkbox
        self.generate_checkbox(0, "Time")

        # check leaks checkbox
        self.generate_checkbox(1, "Leaks")

        # check logs checkbox
        self.generate_checkbox(2, "Logs")

    def generate_checkbox(self, checkbox_column, checkbox_text):
        # generate single checkbox in checkbox row
        self.checkbox = ctk.CTkCheckBox(self.import_file_frame, text=checkbox_text,
                                        variable=self.checkbox_vars[checkbox_column], border_width=2)
        self.checkbox.grid(row=1, column=checkbox_column, padx=10, pady=10)

    def generate_testcase_container(self):
        # frame for testcase
        self.infile_frame = ctk.CTkFrame(self)
        self.infile_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.infile_label = ctk.CTkLabel(self.infile_frame, text="Import file with input or modify textbox")
        self.infile_label.grid(row=1, column=0, padx=20, pady=10)
        self.infile_button = ctk.CTkButton(self.infile_frame, text="Choose file", fg_color="transparent",
                                           border_width=2, command=self.controller.open_testcase_file)
        self.infile_button.grid(row=1, column=1, padx=20, pady=10)
        self.run_button = ctk.CTkButton(self.infile_frame, text="RUN", width=100, command=self.controller.run)
        self.run_button.grid(row=1, column=2, padx=10, pady=10)
        # input file preview
        self.infile_preview = ctk.CTkTextbox(self, height=200)
        self.infile_preview.grid(row=2, column=0, padx=20, pady=10, sticky="new")

    def generate_output_frame(self, text):
        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.grid(row=3, column=0, columnspan=3, padx=20, pady=10, sticky="nesw")
        self.output_button = ctk.CTkButton(self.output_frame, text="Get results",
                                           border_width=2, command=lambda: self.generate_output_window(text))
        self.output_button.grid(row=3, column=0, padx=10, pady=10)

    def generate_output_window(self, text):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ctk.CTkToplevel(self)
            self.toplevel_window.rowconfigure(0, weight=1)
            self.toplevel_window.columnconfigure(0, weight=1)
            self.toplevel_window.title("results preview")
            self.toplevel_window.geometry("810x600")
            self.output_preview = ctk.CTkTextbox(self.toplevel_window)
            self.output_preview.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

            self.output_preview.delete("0.0", tkinter.END)
            self.output_preview.insert(tkinter.END, text)
        else:
            self.toplevel_window.focus()
