import customtkinter as ctk
import tkinter


def generate_popup_window(message, view):
    error_window = ctk.CTkToplevel(view)
    error_window.title("Error")
    error_window.geometry("200x50")
    error_window.rowconfigure(0, weight=1)
    error_window.columnconfigure(0, weight=1)
    error_textbox = ctk.CTkTextbox(error_window)
    error_textbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    error_textbox.insert(tkinter.END, message)
    error_textbox.configure(state="disabled")
