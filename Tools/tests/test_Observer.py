import unittest
from unittest.mock import MagicMock, patch
from Tools import FileObserver


class Test_Observer(unittest.TestCase):

    def setUp(self):
        self.instance = FileObserver.FileObserver.get_instance()

    def tearDown(self):
        self.instance._FileObserver__subscribers = []

    def test_call_get_instance_twice(self):
        instance2 = FileObserver.FileObserver.get_instance()
        self.assertEqual(self.instance, instance2)

    def test_calling_constructor_directly(self):
        with self.assertRaises(Exception):
            FileObserver.FileObserver()

    def test_subscribes_are_empty(self):
        self.assertEqual(self.instance._FileObserver__subscribers, [])

    def test_add_subscriber(self):
        self.instance.add_subscriber("test")
        self.assertEqual(self.instance._FileObserver__subscribers, ["test"])

    @patch('builtins.print', new_callable=MagicMock)
    def test_notify_when_sub_not_implemented_update_code(self, mock_print):
        sub = MagicMock()
        sub.controller.update_code = MagicMock(call_arg=0, side_effect=AttributeError)

        self.instance.add_subscriber(sub)
        self.instance.notify(0)

        mock_print.assert_called_once_with("Not implemented yet")

    def test_notify_when_sub_implemented_update_code(self):
        sub = MagicMock()
        sub.controller.update_code = MagicMock(call_arg=0)

        self.instance.add_subscriber(sub)
        self.instance.notify(0)

        sub.controller.update_code.assert_called_once_with(0)
