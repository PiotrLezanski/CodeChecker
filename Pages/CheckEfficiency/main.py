import tkinter
import customtkinter as ctk
from MainWindow import *

#TODO: import other files
from page1 import *


class CodeCheckerApp(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("green")

        super().__init__()
        self.title("C++ Code Checker")
        self.geometry("810x500")

    # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(3, weight=1)

    # sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="CodeChecker", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)
        self.scale_label = ctk.CTkLabel(self.sidebar_frame, text="zoom")
        self.scale_label.grid(row=7, column=0, padx=10)
        self.scale_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_window_scale)
        self.scale_menu.grid(row=8, column=0, padx=10, pady=(5,10))

    # menu
        # TODO: add another applications/frames to menu
        self.menu_buttons = []
        self.get_output_button = ctk.CTkButton(self.sidebar_frame, text="Get Output", command=lambda: self.show_frame(MainWindow))
        self.get_output_button.grid(row=1, column=0, pady=10)
        self.page2_button = ctk.CTkButton(self.sidebar_frame, text="Page1", command=lambda: self.show_frame(Page2))
        self.page2_button.grid(row=2, column=0, pady=10)
        self.page3_button = ctk.CTkButton(self.sidebar_frame, text="Page2", command=lambda: self.show_frame(Page3))
        self.page3_button.grid(row=3, column=0, pady=10)
        self.menu_buttons.append(self.get_output_button)
        self.menu_buttons.append(self.page2_button)
        self.menu_buttons.append(self.page3_button)

    # container
        container = ctk.CTkFrame(self)
        container.grid(row=0, column=1, sticky="nsew")

    # list of pages
        self.frames = {}
        for Page in (MainWindow, Page2, Page3): # add another pages
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=1, sticky="nsew")

        self.show_frame(MainWindow)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def change_window_scale(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
        new_geom = str(int(new_scaling_float*810)) + 'x' + str(int(new_scaling_float*500))
        self.geometry(new_geom)

    def set_active(self, page):
        # TODO: dont forget do add new buttons
        self.get_output_button._bg_color = ""


if __name__ == "__main__":
    app = CodeCheckerApp()
    app.mainloop()
