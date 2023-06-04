import customtkinter as ctk


class Controller:
    def __init__(self, view):
        self.view = view

    def load_file(self, text_box):
        print(text_box)
        # operate with singleton
