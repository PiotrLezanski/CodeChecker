import customtkinter as ctk
from Pages.Main.model import Model

DEFAULT = "#2fa572"
HOVER = "#106a43"


class Controller:
    def __init__(self, view):
        self.view = view
        self.model = Model(self)
        self.frames = {}

    def load_frames(self, container):
        pages = self.model.load_pages()
        for page in pages:
            frame = page(container)
            frame.grid(row=0, column=0, sticky="nsew")
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)
            self.frames[page] = frame

    @staticmethod
    def generate_button(frame, position, name, expression):
        button = ctk.CTkButton(frame, text=name, command=expression)
        button.grid(row=position, column=0, pady=10)
        return button

    def button_on_click(self, button_id, page):
        self.disable_button(button_id)
        self.show_frame(page)

    def disable_button(self, button_id):
        clicked = self.view.buttons[button_id - 1]
        for button in self.view.buttons:
            button.configure(state="normal", fg_color=DEFAULT)
        clicked.configure(state="disabled", fg_color=HOVER)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
