import customtkinter as ctk
from Pages.Main.model import Model


class Controller:
    def __init__(self, view):
        self.view = view
        self.model = Model(self)
        self.frames = {}

    def load_frames(self, container, parent):
        pages = self.model.load_pages()
        for page in pages:
            frame = page(container, parent)
            frame.grid(row=0, column=0, sticky="nsew")
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)
            self.frames[page] = frame

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    @staticmethod
    def generate_button(frame, position, name, expression):
        get_output_button = ctk.CTkButton(frame, text=name, command=expression)
        get_output_button.grid(row=position, column=0, pady=10)
