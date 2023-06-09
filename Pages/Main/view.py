import customtkinter as ctk
from Pages.Main.controller import Controller
from Pages.WelcomeWindow.view import View as WelcomeView
from Pages.Settings.view import View as SettingsView
from Pages.GetOutput.view import View as GetOutputView
from Pages.CheckEfficiency.view import View as EfficiencyView
from Pages.CodeCompare.view import View as CompareView
from Pages.TestPass.view import View as TestPassView
from Pages.CodeDifference.view import View as CodeDifferenceView

class View(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("C++ Code Checker")
        self.geometry("810x600")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.sidebar_frame = None
        self.container = None
        self.buttons = []
        self.controller = Controller(self)

        self.configure_grid_layout()
        self.configure_container()
        self.controller.load_frames(self.container)
        self.generate_buttons_menu()
        self.controller.button_on_click(1, WelcomeView)

    def generate_buttons_menu(self):
        buttons_info = [
            (1, "Welcome", lambda: self.controller.button_on_click(1, WelcomeView)),
            (2, "Get output", lambda: self.controller.button_on_click(2, GetOutputView)),
            (3, "Efficiency checker", lambda: self.controller.button_on_click(3, EfficiencyView)),
            (4, "Code compare", lambda: self.controller.button_on_click(4, CompareView)),
            (5, "Code difference", lambda: self.controller.button_on_click(5, CodeDifferenceView)),
            (6, "Test pass", lambda: self.controller.button_on_click(6, TestPassView)),
            (8, "Settings", lambda: self.controller.button_on_click(7, SettingsView))
        ]
        self.buttons = []
        for row, text, command in buttons_info:
            button = self.controller.generate_button(self.sidebar_frame, row, text, command)
            self.buttons.append(button)

    def configure_grid_layout(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.configure_sidebar()

    def configure_container(self):
        self.container = ctk.CTkFrame(self, border_width=10)
        self.container.grid(row=0, column=1, rowspan=10, sticky="nsew")

    def configure_sidebar(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=150)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(1, weight=1)
        self.sidebar_frame.grid_rowconfigure(7, weight=1)
        logo_label = ctk.CTkLabel(self.sidebar_frame,
                                  text="CodeChecker",
                                  font=ctk.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=20)