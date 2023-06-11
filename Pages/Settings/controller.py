import customtkinter as ctk


class Controller:
    def __init__(self, view):
        self.view = view

    @staticmethod
    def change_appearance_mode(value):
        value = value.get()
        if value == "dark":
            ctk.set_appearance_mode("dark")
        elif value == "light":
            ctk.set_appearance_mode("light")

    def change_window_scale(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
        new_geom = str(int(new_scaling_float*810)) + 'x' + str(int(new_scaling_float*500))
        self.view.master.master.geometry(new_geom)
