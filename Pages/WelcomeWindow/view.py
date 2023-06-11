import customtkinter as ctk
from Pages.WelcomeWindow.controller import Controller

MAIN_TEXT = """
Welcome to CodeChecker!
Currently supported programming languages: C++

Upload your code below and set the default one for tests. Add another code to compare those two.
To change the theme and interface size, please use Settings 
To change page to desired functionality, please use the sidebar placed on the left and upload required files.
"""


class View(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = Controller(self)
        self.checkboxes = []
        self.text_boxes = []
        self.labels = []

        self.content = ctk.CTkFrame(self)
        self.content.pack(fill="x", padx=20, pady=20)

        self.generate_message()
        self.generate_codes()
        self.checkboxes[0].select()

    def generate_message(self):
        text_box = ctk.CTkTextbox(self.content, wrap="word")
        text_box.insert("0.0", MAIN_TEXT)
        text_box.configure(state="disabled")
        text_box.pack(fill="both", expand=1)

    def generate_codes(self):
        grid = ctk.CTkFrame(self.content)
        self.generate_single_code(grid, 0, 0)
        self.generate_single_code(grid, 2, 1)
        grid.grid_columnconfigure(0, weight=1)
        grid.grid_columnconfigure(2, weight=1)
        grid.pack(fill="x", expand=1, padx=20, pady=20)

    def generate_single_code(self, grid, column_number, _id):
        checkbox = ctk.CTkCheckBox(grid, text="Set as default",
                                   command=lambda: self.controller.update_checkboxes(checkbox))
        self.checkboxes.append(checkbox)
        checkbox.grid(row=0, column=column_number, padx=5, pady=5)

        label = ctk.CTkLabel(grid, text="")
        self.labels.append(label)
        label.grid(row=1, column=column_number, columnspan=2, sticky="nsew", padx=2, pady=2)

        file_button = ctk.CTkButton(grid, text="Choose file", fg_color="transparent", border_width=2,
                                    command=lambda: self.controller.load_file(_id, label))
        file_button.grid(row=0, column=column_number + 1, padx=5, pady=5)

        text_box = ctk.CTkTextbox(grid, wrap="word")
        self.text_boxes.append(text_box)
        text_box.grid(row=2, column=column_number, columnspan=2, sticky="nsew", padx=10, pady=10)
