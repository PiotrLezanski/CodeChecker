import unittest
from Tools import FileSingleton


class TestFileSingleton(unittest.TestCase):
    instance = FileSingleton.FileSingleton.get_instance()

    def test_get_instance(self):
        self.assertIsInstance(self.instance, FileSingleton.FileSingleton)

    def test_call_get_instance_twice(self):
        instance2 = FileSingleton.FileSingleton.get_instance()
        self.assertEqual(self.instance, instance2)

    def test_calling_constructor_directly(self):
        with self.assertRaises(Exception):
            FileSingleton.FileSingleton()
