class WrongExtensionError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class SameFilesError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
