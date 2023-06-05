from Pages.Main.view import View


class App:
    def __init__(self):
        super().__init__()
        self.main_view = View()

    def run(self):
        self.main_view.mainloop()


if __name__ == "__main__":
    app = View()
    app.mainloop()