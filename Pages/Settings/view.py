import customtkinter as ctk
from Pages.Settings.controller import Controller


class View(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.controller = Controller(self)

        self.value_label = None
        self.slider = None

        content = ctk.CTkFrame(self, width=550)
        self.generate_zoom_option(content)
        self.generate_theme_switch(content)
        content.pack(fill="x", expand=1, padx=20, pady=20)

    def generate_zoom_option(self, container):
        scale_label = ctk.CTkLabel(container, text="Zoom",
                                   font=ctk.CTkFont(size=20, weight="bold"))
        scale_label.pack(fill="x", expand=1)
        scale_menu = ctk.CTkOptionMenu(container,
                                       values=["100%", "80%", "90%", "110%", "120%"],
                                       command=self.controller.change_window_scale)
        scale_menu.pack(fill="y", expand=1, padx=20, pady=20)

    def generate_theme_switch(self, container):
        switch_value = ctk.StringVar(value="dark")
        switch = ctk.CTkSwitch(container,
                               text="Switch mode",
                               command=lambda: self.controller.change_appearance_mode(switch_value),
                               variable=switch_value,
                               onvalue="dark", offvalue="light")
        switch.pack(fill="y", expand=1, padx=20, pady=20)

    # def generate_font_size_slider(self, container):
    #     label = ctk.CTkLabel(container, text="Font size",
    #                          font=ctk.CTkFont(size=20, weight="bold"))
    #     label.pack(fill="y", expand=1, padx=20, pady=20)
    #
    #     self.slider = ctk.CTkSlider(container, from_=6, to=30, number_of_steps=12,
    #                                 command=lambda value: self.controller.slider_on_change(value))
    #     self.slider.set(12)
    #     self.slider.pack(fill="x", expand=1, padx=20, pady=20)
    #
    #     self.value_label = ctk.CTkLabel(container, text="12")
    #     self.value_label.pack(padx=20, pady=20)
