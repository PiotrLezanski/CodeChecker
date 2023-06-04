import customtkinter as ctk

from Pages.Main.view import View


class App(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")
        super().__init__()
        main_view = View()
        main_view.mainloop()


if __name__ == "__main__":
    app = App()
    app.mainloop()
