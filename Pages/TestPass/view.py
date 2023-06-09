import tkinter.ttk
import customtkinter as ctk
from Pages.TestPass.controller import Controller
from Tools.FileSingleton import FileSingleton

class View(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)
        self.columnconfigure(0, weight=1)

        self.testcases_frame = None
        self.run_all_button = None
        self.run_test_buttons = None
        self.output_texts = None
        self.output_labels = None
        self.separators = None
        self.input_texts = None
        self.input_labels = None
        self.testcase_frames = None
        self.number_of_tests = None
        self.toplevel_window = None
        self.singleton = FileSingleton.get_instance()
        self.controller = Controller(self)

        self.import_file_frame = ctk.CTkFrame(self)
        self.import_file_frame.columnconfigure(0, weight=1)
        self.import_file_frame.columnconfigure(1, weight=0)
        self.import_file_frame.columnconfigure(2, weight=1)
        self.import_file_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # import source file
        self.import_source_label = ctk.CTkLabel(self.import_file_frame, text="Import source code")
        self.import_source_label.grid(row=0, column=0, padx=10, pady=10)
        self.import_source_button = ctk.CTkButton(self.import_file_frame, text="Choose file", fg_color="transparent",
                                                  border_width=2, command=self.controller.open_source_file)
        self.import_source_button.grid(row=0, column=1, padx=10, pady=10)

        # display file name
        if self.singleton.get_filepath() is None:
            text = "No file uploaded"
        else:
            text = self.singleton.get_filepath()[self.singleton.get_filepath().rfind('/'):]

        self.file_name = ctk.CTkLabel(self.import_file_frame, text=text)
        self.file_name.grid(row=0, column=2, padx=10, pady=10)

        # number of tests
        self.test_number_label = ctk.CTkLabel(self.import_file_frame, text="Number of testcases")
        self.test_number_label.grid(row=1, column=0, padx=10, pady=10)
        self.test_number_entry = ctk.CTkEntry(self.import_file_frame, placeholder_text="max. 10")
        self.test_number_entry.grid(row=1, column=1, padx=10, pady=10)
        self.load_tests_button = ctk.CTkButton(self.import_file_frame, text="Load tests", command=self.controller.load_tests)
        self.load_tests_button.grid(row=1, column=2, padx=10, pady=10)

    def create_testcase_components(self):
        # create RUN ALL button
        self.run_all_button = ctk.CTkButton(self, text="RUN ALL TESTS", command=self.controller.run_all_testcases, width=300)
        self.run_all_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.testcase_frames = [None] * int(self.number_of_tests)
        self.input_labels = [None] * int(self.number_of_tests)
        self.input_texts = [None] * int(self.number_of_tests)
        self.separators = [None] * int(self.number_of_tests)
        self.output_labels = [None] * int(self.number_of_tests)
        self.output_texts = [None] * int(self.number_of_tests)
        self.run_test_buttons = [None] * int(self.number_of_tests)

        self.testcases_frame = ctk.CTkScrollableFrame(self, width=600, height=415)
        self.testcases_frame.grid(row=3, column=0, pady=10)
        self.testcases_frame.columnconfigure(0, weight=1)
        self.testcases_frame.columnconfigure(1, weight=1)
        for i in range(int(self.number_of_tests)):
            self.testcase_frames[i] = ctk.CTkFrame(self.testcases_frame, border_width=2)
            self.input_labels[i] = ctk.CTkLabel(self.testcase_frames[i], text="Input")
            self.input_texts[i] = ctk.CTkTextbox(self.testcase_frames[i], height=60, width=460)
            self.separators[i] = tkinter.ttk.Separator(self.testcase_frames[i], orient="horizontal", style='TSeparator')
            self.output_labels[i] = ctk.CTkLabel(self.testcase_frames[i], text="Expected output")
            self.output_texts[i] = ctk.CTkTextbox(self.testcase_frames[i], height=50)
            self.run_test_buttons[i] = ctk.CTkButton(self.testcase_frames[i], text="Run test", fg_color="transparent", border_width=2, command=lambda x = i: self.controller.run_testcase(x))

    def generate_testcase_frame(self, elements, row):
        self.testcase_frames[elements].grid(row=row, column=0, padx=10, pady=10, sticky="nsew")
        self.testcase_frames[elements].grid_columnconfigure(0, weight=1)
        self.testcase_frames[elements].grid_columnconfigure(1, weight=1)
        self.testcase_frames[elements].grid_columnconfigure(2, weight=1)
        # input
        self.input_labels[elements].grid(row=0, column=0, padx=10, pady=10)
        self.input_texts[elements].grid(row=0, column=1, sticky="ew")
        # separator
        self.separators[elements].grid(row=1, column=0)
        # expected output
        self.output_labels[elements].grid(row=2, column=0, padx=10, pady=10)
        self.output_texts[elements].grid(row=2, column=1, sticky="ew")
        # run button
        self.run_test_buttons[elements].grid(row=3, sticky="nsew", padx=20, columnspan=2)

    def hide_testcases(self):
        for i in range(int(self.number_of_tests)):
            self.testcase_frames[i].grid_remove()
            self.input_labels[i].grid_remove()
            self.input_texts[i].grid_remove()
            self.separators[i].grid_remove()
            self.output_labels[i].grid_remove()
            self.output_texts[i].grid_remove()
            self.run_test_buttons[i].grid_remove()