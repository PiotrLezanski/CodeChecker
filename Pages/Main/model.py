from Tools.FileObserver import FileObserver
from Pages.WelcomeWindow.view import View as WelcomeView
from Pages.Settings.view import View as SettingsView
from Pages.GetOutput.view import View as GetOutputView
from Pages.CheckEfficiency.view import View as EfficiencyView
from Pages.CodeCompare.view import View as CompareView
from Pages.TestPass.view import View as TestPassView
from Pages.CodeDifference.view import View as CodeDifferenceView

class Model:
    def __init__(self, controller):
        self.controller = controller
        self.observer = FileObserver.get_instance()

    def load_pages(self, container):
        frames = {}
        for page in (WelcomeView, GetOutputView, EfficiencyView, CompareView, CodeDifferenceView, TestPassView, SettingsView):
            frame = page(container)
            frame.grid(row=0, column=0, sticky="nsew")
            self.observer.add_subscriber(frame)
            frames[page] = frame
        return frames
