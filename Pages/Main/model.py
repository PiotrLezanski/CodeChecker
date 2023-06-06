from Pages.WelcomeWindow.view import View as WelcomeView
from Pages.Settings.view import View as SettingsView
from Pages.GetOutput.view import View as GetOutputView
from Pages.CheckEfficiency.view import View as EfficiencyView
from Pages.CodeCompare.view import View as CompareView
from Pages.TestPass.view import View as TestPassView

class Model:
    def __init__(self, controller):
        self.controller = controller

    @staticmethod
    def load_pages():
        frames = {}
        for page in (WelcomeView, GetOutputView, CompareView, EfficiencyView, TestPassView, SettingsView):
            frames[page] = page
        return frames
