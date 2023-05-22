import tkinter as tk
import customtkinter as ctk
  
class Page2(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.label = ctk.CTkLabel(self, text="PAGE11111")
        self.label.grid(row=0, column=0, padx=10, pady=20)

class Page3(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.label = ctk.CTkLabel(self, text="PAGE22222")
        self.label.grid(row=0, column=0, padx=10, pady=20)