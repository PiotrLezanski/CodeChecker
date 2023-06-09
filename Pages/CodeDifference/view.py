from Pages.CodeDifference.controller import Controller
from Tools.FileSingleton import FileSingleton
import customtkinter as ctk
import tkinter


class View(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)

        self.output_preview = None
        self.toplevel_window = None
        self.output_button = None
        self.output_frame = None
        self.run_button = None
        self.check_label = None
        self.check_container = None
        self.second_file_name = None
        self.import_second_source_button = None
        self.import_second_source_label = None
        self.first_file_name = None
        self.import_first_source_button = None
        self.import_first_source_label = None
        self.import_file_frame = None
        self.controller = Controller(self)

        #self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # input filer container
        self.generate_file_container()

        # check difference container
        self.generate_check_container()

    def generate_file_container(self):
        self.import_file_frame = ctk.CTkFrame(self)
        self.import_file_frame.rowconfigure(0, weight=1)
        self.import_file_frame.columnconfigure(0, weight=1)
        self.import_file_frame.columnconfigure(1, weight=1)
        self.import_file_frame.columnconfigure(2, weight=1)
        self.import_file_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.generate_first_file_information()
        self.generate_second_file_information()

    def generate_first_file_information(self):
        self.import_first_source_label = ctk.CTkLabel(self.import_file_frame, text="Import first source code")
        self.import_first_source_label.grid(row=0, column=0, padx=10, pady=10)
        self.import_first_source_button = ctk.CTkButton(self.import_file_frame, text="Choose file",
                                                        fg_color="transparent", border_width=2,
                                                        command=lambda: self.controller.load_source_file(0))
        self.import_first_source_button.grid(row=0, column=1, padx=10, pady=10)

        self.generate_first_file_name()

    def generate_first_file_name(self, singleton=FileSingleton.get_instance()):
        info_about_file = "No file" if singleton.get_filepath(0) == "" else str(singleton.get_filepath(0))
        self.first_file_name = ctk.CTkLabel(self.import_file_frame, text=info_about_file)
        self.first_file_name.grid(row=0, column=2, padx=10, pady=10)

    def generate_second_file_information(self):
        self.import_second_source_label = ctk.CTkLabel(self.import_file_frame, text="Import second source code")
        self.import_second_source_label.grid(row=1, column=0, padx=10, pady=10)
        self.import_second_source_button = ctk.CTkButton(self.import_file_frame, text="Choose file",
                                                         fg_color="transparent", border_width=2,
                                                         command=lambda: self.controller.load_source_file(1))
        self.import_second_source_button.grid(row=1, column=1, padx=10, pady=10)

        self.generate_second_file_name()

    def generate_second_file_name(self, singleton=FileSingleton.get_instance()):
        info_about_file = "No file" if singleton.get_filepath(1) == "" else str(singleton.get_filepath(1))
        self.second_file_name = ctk.CTkLabel(self.import_file_frame, text=info_about_file)
        self.second_file_name.grid(row=1, column=2, padx=10, pady=10)

    def generate_check_container(self):
        self.check_container = ctk.CTkFrame(self)
        self.check_container.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.check_container.columnconfigure(0, weight=1)
        self.check_container.columnconfigure(1, weight=1)

        self.check_label = ctk.CTkLabel(self.check_container, text="Check difference")
        self.check_label.grid(row=1, column=0, padx=10, pady=10)

        self.run_button = ctk.CTkButton(self.check_container, text="RUN", border_width=2,
                                        command=lambda: self.controller.run())
        self.run_button.grid(row=1, column=1, padx=10, pady=10)

    def generate_output_frame(self, text):
        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        self.output_button = ctk.CTkButton(self.output_frame, text="Get results",
                                           border_width=2, command=lambda: self.generate_output_window(text))
        self.output_button.grid(row=4, column=0, padx=20, pady=10)

    def generate_output_window(self, text):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ctk.CTkToplevel(self)
            self.toplevel_window.rowconfigure(0, weight=1)
            self.toplevel_window.columnconfigure(0, weight=1)
            self.toplevel_window.columnconfigure(1, weight=1)
            self.toplevel_window.title("results preview")
            self.toplevel_window.geometry("810x600")

            self.output_preview = ctk.CTkTextbox(self.toplevel_window, width=100, height=100)
            self.output_preview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

            self.output_preview.delete("0.0", tkinter.END)
            self.output_preview.insert(tkinter.END, text)

        else:
            self.toplevel_window.focus()