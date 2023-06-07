from tkinter import filedialog
from Tools.FileSingleton import FileSingleton


class Controller:
    def __init__(self, view):
        self.view = view
        self.singleton = FileSingleton.get_instance()

    def load_file(self, _id, label):
        filepath = filedialog.askopenfilename(title="Choose a code file",
                                              initialdir="/",
                                              filetypes=[(".cpp", "*.cpp")])
        if filepath != "":
            self.singleton.set_file(filepath, _id)
            file_name = self.singleton.get_filename(_id)
            file_code = self.singleton.get_file_text(_id)
            label.configure(text=file_name)
            self.view.text_boxes[_id].insert("0.0", file_code)

    def update_checkboxes(self, recently_used):
        for checkbox in self.view.checkboxes:
            checkbox.deselect()
        recently_used.select()
        chosen = self.view.checkboxes.index(recently_used)
        self.singleton.set_default(chosen)

    def update_code(self, _id):
        boxes = self.view.text_boxes
        if len(boxes) > _id:
            boxes[_id].insert("0.0", self.singleton.get_file_text(_id))
