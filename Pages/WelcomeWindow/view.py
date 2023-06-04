import customtkinter as ctk
from Pages.WelcomeWindow.controller import Controller


class View(ctk.CTkFrame):
    def __init__(self, master, controller):
        ctk.CTkFrame.__init__(self, master)
        self.controller = Controller(self)

        self.content = ctk.CTkFrame(self)
        self.content.pack(fill="x", padx=20, pady=20)

        self.generate_message()
        self.generate_codes()

    def generate_message(self):
        text_box = ctk.CTkTextbox(self.content, wrap="word")
        text_box.insert("0.0",
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent porttitor egestas nunc ut efficitur. Morbi iaculis, urna in pretium convallis, ante quam efficitur nibh, eu volutpat leo erat nec mi. Curabitur convallis turpis mauris, nec rutrum dolor consequat quis. Suspendisse potenti. Nam auctor ultricies velit in sollicitudin. Praesent congue, libero.")
        text_box.configure(state="disabled")
        text_box.pack(fill="both", expand=1)

    def generate_codes(self):
        grid = ctk.CTkFrame(self.content)
        self.generate_single_code(grid, 0)
        self.generate_single_code(grid, 2)
        grid.grid_columnconfigure(0, weight=1)
        grid.grid_columnconfigure(2, weight=1)
        grid.pack(fill="x", expand=1, padx=20, pady=20)

    def generate_single_code(self, grid, column_number):
        label = ctk.CTkLabel(grid, text="Code preview")
        label.grid(row=0, column=column_number, sticky="nsew", padx=10, pady=10)
        text_box = ctk.CTkTextbox(grid, wrap="word")
        text_box.grid(row=1, column=column_number, columnspan=2, sticky="nsew", padx=10, pady=10)
        file_button = ctk.CTkButton(grid, text="Choose file", fg_color="transparent", border_width=2,
                                    command=lambda: self.controller.load_file(text_box))
        file_button.grid(row=0, column=column_number + 1)
