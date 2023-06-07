from Tools.Exceptions import WrongExtensionError


class FileSingleton(object):
    __instance = None
    __file = [None, None]
    __filepath = [None, None]
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

    def set_default(self, i):
        if i == 0 or i == 1:
            FileSingleton.__default = i

    def get_default(self):
        return FileSingleton.__default

    def get_file(self, i=None):
        if i is None:
            i = FileSingleton.__default
        return FileSingleton.__file[i]

    def get_file_text(self, i=None):
        if i is None:
            i = FileSingleton.__default
        if FileSingleton.__file[i] is not None:
            return FileSingleton.__file[i].read()

    def get_filepath(self, i=None):
        if i is None:
            i = FileSingleton.__default
        return FileSingleton.__filepath[i]

    # before reading new file close old file
    # if wrong extension, raise exception WrongExtensionError
    # if you cant use WrongExtensionError, type from Tools.Exceptions import WrongExtensionError
    # if wrong path, raise exception FileNotFoundError
    def set_file(self, file_path, i=None):
        if i is None:
            i = FileSingleton.__default
        if file_path.endswith(".cpp") or file_path.endswith(".h"):
            backup = FileSingleton.__filepath[i]

            try:
                FileSingleton.__close_file(i)

                # I'm not sure if I should check if file1 and file2 are the same

                # if FileSingleton.__filepath[k] == file_path:
                #     raise SameFilesError("File1 and file2 cannot be the same")

                FileSingleton.__file[i] = open(file_path, 'r')
                FileSingleton.__filepath[i] = file_path
            except Exception as e:
                if backup is not None:
                    FileSingleton.__file[i] = open(backup, 'r')
                    FileSingleton.__filepath[i] = backup
                raise e
        else:
            raise WrongExtensionError("File must be a .cpp or .h file")

    def __close_file(self, i=None):
        if i is None:
            i = FileSingleton.__default
        if FileSingleton.__file[i] is not None:
            FileSingleton.__file[i].close()
            FileSingleton.__file[i] = None
            FileSingleton.__filepath[i] = None

    def reset(self):
        if FileSingleton.__file[0] is not None:
            FileSingleton.__close_file(0)
        if FileSingleton.__file[1] is not None:
            FileSingleton.__close_file(1)
        FileSingleton.__file[0] = None
        FileSingleton.__file[1] = None
        FileSingleton.__filepath[0] = None
        FileSingleton.__filepath[1] = None
        FileSingleton.__default = 0

    def reset_reading_position(self, i=None):
        if i is None:
            i = FileSingleton.__default
        if FileSingleton.__file[i] is not None:
            FileSingleton.__file[i].seek(0)
