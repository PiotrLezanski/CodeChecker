from Tools.Exceptions import WrongExtensionError
from typing import Optional, IO


class FileSingleton(object):
    __instance = None
    __file1: Optional[IO] = None  # file1 is the left file
    __file2: Optional[IO] = None  # file2 is the right file
    __filepath1: Optional[str] = None
    __filepath2: Optional[str] = None

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
    def get_file1():
        return FileSingleton.__file1

    @staticmethod
    def get_file2():
        return FileSingleton.__file2

    @staticmethod
    def get_file1_text():
        return FileSingleton.__file1.read()

    @staticmethod
    def get_file2_text():
        return FileSingleton.__file2.read()

    @staticmethod
    def get_filepath1():
        return FileSingleton.__filepath1

    @staticmethod
    def get_filepath2():
        return FileSingleton.__filepath2

    # before reading new file close old file
    # if wrong extension, raise exception WrongExtensionError
    # if you cant use WrongExtensionError, type from Tools.Exceptions import WrongExtensionError
    # if wrong path, raise exception FileNotFoundError
    @staticmethod
    def set_file1(file_path):
        if file_path.endswith(".cpp") or file_path.endswith(".h"):
            try:
                FileSingleton.__close_file1()

                # I'm not sure if I should check if file1 and file2 are the same

                # if FileSingleton.__filepath2 == file_path:
                #     raise SameFilesError("File1 and file2 cannot be the same")

                FileSingleton.__file1 = open(file_path, 'r')
                FileSingleton.__filepath1 = file_path
            except Exception as e:
                raise e
        else:
            raise WrongExtensionError("File must be a .cpp or .h file")

    # before reading new file close old file if and only if new path is correct
    # if wrong extension, raise exception WrongExtensionError
    # if you cant use WrongExtensionError, type from Tools.Exceptions import WrongExtensionError
    # if wrong path, raise exception FileNotFoundError
    @staticmethod
    def set_file2(file_path):
        if file_path.endswith(".cpp") or file_path.endswith(".h"):
            try:
                FileSingleton.__close_file2()

                # I'm not sure if I should check if file1 and file2 are the same

                # if FileSingleton.__filepath1 == file_path:
                #     raise SameFilesError("File1 and file2 cannot be the same")

                FileSingleton.__file2 = open(file_path, 'r')
                FileSingleton.__filepath2 = file_path
            except Exception as e:
                raise e
        else:
            raise WrongExtensionError("File must be a .cpp or .h file")

    @staticmethod
    def __close_file1():
        if FileSingleton.__file1 is not None:
            FileSingleton.__file1.close()
            FileSingleton.__path1 = None

    @staticmethod
    def __close_file2():
        if FileSingleton.__file2 is not None:
            FileSingleton.__file2.close()
            FileSingleton.__path2 = None

    @staticmethod
    def reset():
        if FileSingleton.__file1 is not None:
            FileSingleton.__close_file1()
        if FileSingleton.__file2 is not None:
            FileSingleton.__close_file2()
        FileSingleton.__file1 = None
        FileSingleton.__file2 = None
        FileSingleton.__filepath1 = None
        FileSingleton.__filepath2 = None