from Tools.Exceptions import WrongExtensionError
from typing import Optional, IO


class FileSingleton(object):
    __instance = None
    __file = [Optional[IO], Optional[IO]]
    __filepath = [Optional[str], Optional[str]]
    __default = 0

    def __init__(self):
        if FileSingleton.__instance is not None:
            raise Exception("Direct initialization of singleton is not allowed. Use get_instance() instead.")
        else:
            FileSingleton.__instance = self
            
    @staticmethod
    def get_instance():
        if FileSingleton.__instance is None:
            FileSingleton()
        return FileSingleton.__instance

    @staticmethod
    def set_default(i):
        FileSingleton.__default = i

    @staticmethod
    def get_file(i=__default):
        return FileSingleton.__file[i]

    @staticmethod
    def get_file_text(i=__default):
        return FileSingleton.__file[i].read()

    @staticmethod
    def get_filepath(i=__default):
        return FileSingleton.__filepath[i]

    # before reading new file close old file
    # if wrong extension, raise exception WrongExtensionError
    # if you cant use WrongExtensionError, type from Tools.Exceptions import WrongExtensionError
    # if wrong path, raise exception FileNotFoundError
    @staticmethod
    def set_file(file_path, i=__default):
        if file_path.endswith(".cpp") or file_path.endswith(".h"):
            try:
                FileSingleton.__close_file(i)

                # I'm not sure if I should check if file1 and file2 are the same

                # if FileSingleton.__filepath[k] == file_path:
                #     raise SameFilesError("File1 and file2 cannot be the same")

                FileSingleton.__file[i] = open(file_path, 'r')
                FileSingleton.__filepath[i] = file_path
            except Exception as e:
                raise e
        else:
            raise WrongExtensionError("File must be a .cpp or .h file")

    @staticmethod
    def __close_file(i=__default):
        if FileSingleton.__file[i] is not None:
            FileSingleton.__file[i].close()
            FileSingleton.__path1 = None

    @staticmethod
    def reset():
        if FileSingleton.__file[0] is not None:
            FileSingleton.__close_file(0)
        if FileSingleton.__file[1] is not None:
            FileSingleton.__close_file(1)
        FileSingleton.__file[0] = None
        FileSingleton.__file[1] = None
        FileSingleton.__filepath[0] = None
        FileSingleton.__filepath[1] = None
