import os.path

from Tools.Exceptions import WrongExtensionError
from Tools.FileObserver import FileObserver


class FileSingleton(object):
    __instance = None

    def __init__(self):
        if FileSingleton.__instance is not None:
            raise Exception("Direct initialization of singleton is not allowed. Use get_instance() instead.")
        else:
            FileSingleton.__instance = self
            self.__file = [None, None]
            self.__filepath = [None, None]
            self.__default = 0
            self.observer = FileObserver.get_instance()

    @staticmethod
    def get_instance():
        if FileSingleton.__instance is None:
            FileSingleton()
        return FileSingleton.__instance

    def set_default(self, i):
        if i == 0 or i == 1:
            self.__default = i
            self.observer.notify(i)

    def get_default(self):
        return self.__default

    def get_file(self, i=None):
        if i is None:
            i = self.__default
        return self.__file[i]

    def get_file_text(self, i=None):
        if i is None:
            i = self.__default
        if self.__file[i] is not None:
            return self.__file[i].read()
        else:
            return ""

    def get_filepath(self, i=None):
        if i is None:
            i = self.__default
        if self.__filepath[i] is not None:
            return self.__filepath[i]
        return ""

    def get_filename(self, i=None):
        if i is None:
            i = self.__default
        if self.__filepath[i] is not None:
            return os.path.basename(self.__filepath[i])
        return ""

    # before reading new file close old file
    # if wrong extension, raise exception WrongExtensionError
    # if you cant use WrongExtensionError, type from Tools.Exceptions import WrongExtensionError
    # if wrong path, raise exception FileNotFoundError
    def set_file(self, file_path, i=None):
        if i is None:
            i = self.__default
        if file_path.endswith(".cpp") or file_path.endswith(".h"):
            backup = self.__filepath[i]

            try:
                self.__close_file(i)

                # I'm not sure if I should check if file1 and file2 are the same

                # if self.__filepath[k] == file_path:
                #     raise SameFilesError("File1 and file2 cannot be the same")

                self.__file[i] = open(file_path, 'r')
                self.__filepath[i] = file_path
            except Exception as e:
                if backup is not None:
                    self.__file[i] = open(backup, 'r')
                    self.__filepath[i] = backup
                raise e
            finally:
                self.observer.notify(i)
        else:
            raise WrongExtensionError("File must be a .cpp or .h file")

    def __close_file(self, i=None):
        if i is None:
            i = self.__default
        if self.__file[i] is not None:
            self.__file[i].close()
            self.__file[i] = None
            self.__filepath[i] = None

    def reset(self):
        if self.__file[0] is not None:
            self.__close_file(0)
        if self.__file[1] is not None:
            self.__close_file(1)
        self.__file[0] = None
        self.__file[1] = None
        self.__filepath[0] = None
        self.__filepath[1] = None
        self.__default = 0

    def reset_reading_position(self, i=None):
        if i is None:
            i = self.__default
        if self.__file[i] is not None:
            self.__file[i].seek(0)
