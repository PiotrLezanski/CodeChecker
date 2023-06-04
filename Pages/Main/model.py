from Pages.WelcomeWindow.view import View as WelcomeView
from Pages.Settings.view import View as SettingsView


class Model:
    def __init__(self, controller):
        self.controller = controller

    @staticmethod
    def load_pages():
        frames = {}
        for page in (WelcomeView, SettingsView):
            frames[page] = page
        return frames
