import customtkinter as ctk
from Pages.TestPass.controller import Controller

class View(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = Controller(self)

        # import source file
        self.code_frame = ctk.CTkFrame(self)
        self.code_frame.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        self.import_source_label = ctk.CTkLabel(self.code_frame, text="Import source code")
        self.import_source_label.grid(row=1, column=1, padx=10, pady=10, sticky="nw")
        self.import_source_button = ctk.CTkButton(self.code_frame, text="Choose file", fg_color="transparent",
                                                  border_width=2, command=self.controller.open_source_file)
        self.import_source_button.grid(row=1, column=2, padx=10, pady=10, sticky="nw")