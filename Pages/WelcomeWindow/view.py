import customtkinter as ctk


class View(ctk.CTkFrame):
    def __init__(self, master, controller):
        ctk.CTkFrame.__init__(self, master)

        content = ctk.CTkFrame(self)
        content.pack(fill="x", padx=20, pady=20)

        text_box = ctk.CTkTextbox(content, wrap="word")
        text_box.insert("0.0",
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent porttitor egestas nunc ut efficitur. Morbi iaculis, urna in pretium convallis, ante quam efficitur nibh, eu volutpat leo erat nec mi. Curabitur convallis turpis mauris, nec rutrum dolor consequat quis. Suspendisse potenti. Nam auctor ultricies velit in sollicitudin. Praesent congue, libero.")
        text_box.configure(state="disabled")
        text_box.pack(fill="both", expand=1)
