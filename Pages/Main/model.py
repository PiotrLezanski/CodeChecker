from Pages.WelcomeWindow.view import View as WelcomeView
from Pages.Settings.view import View as SettingsView
from Pages.GetOutput.view import View as GetOutputView
from Pages.CheckEfficiency.view import View as EfficiencyView


class Model:
    def __init__(self, controller):
        self.controller = controller

    @staticmethod
    def load_pages():
        frames = {}
        for page in (WelcomeView, GetOutputView, EfficiencyView, SettingsView):
            frames[page] = page
        return frames
