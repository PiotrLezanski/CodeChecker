import unittest
from Tools import FileSingleton
from Tools.Exceptions import WrongExtensionError

class TestFileSingleton(unittest.TestCase):
    instance = FileSingleton.FileSingleton.get_instance()
    second_instance = FileSingleton.FileSingleton.get_instance()
    def test_get_instance(self):
        self.assertIsInstance(self.instance, FileSingleton.FileSingleton)

    def test_call_get_instance_twice(self):
        instance2 = FileSingleton.FileSingleton.get_instance()
        self.assertEqual(self.instance, instance2)

    def test_calling_constructor_directly(self):
        with self.assertRaises(Exception):
            FileSingleton.FileSingleton()

    def test_set_file_path(self):
        self.instance.set_file1("programs\cpp_extentnion.cpp")
        self.assertEqual(self.instance.get_filepath1(), "programs\cpp_extentnion.cpp")
        self.instance.set_file2("programs\h_extentnion.h")
        self.assertEqual(self.instance.get_filepath2(), "programs\h_extentnion.h")

    def test_set_non_cpp_file_path(self):
        with self.assertRaises(WrongExtensionError):
            self.instance.set_file1("programs\txt_extentnion.txt")
    def test_set_unexisting_file_path(self):
        with self.assertRaises(FileNotFoundError):
            self.instance.set_file1("test.cpp")

    def test_whil_change_file_path_close_old_file(self):
        self.instance2.set_file1("programs\cpp_extentnion.cpp")
        self.instance2.set_file1("programs\h_extentnion.h")
        self.assertEqual(self.instance2.get_filepath1(), "programs\h_extentnion.h")
        self.instance2.set_file2("programs\cpp_extentnion.cpp")
        self.instance2.set_file2("programs\h_extentnion.h")
        self.assertEqual(self.instance2.get_filepath2(), "programs\h_extentnion.h")

    def test_while_changing_to_wrong_file_path_close_old_file(self):
        self.instance2.set_file1("programs\cpp_extentnion.cpp")
        with self.assertRaises(WrongExtensionError):
            self.instance2.set_file1("programs\h_extentnion.h")
        self.assertEqual(self.instance2.get_filepath1(), "programs\cpp_extentnion.cpp")
        self.instance2.set_file2("programs\h_extentnion.h")
        with self.assertRaises(WrongExtensionError):
            self.instance2.set_file2("programs\cpp_extentnion.cpp")
        self.assertEqual(self.instance2.get_filepath2(), "programs\h_extentnion.h")