import unittest

from foo import foo_1


class TestBar2(unittest.TestCase):

    def setUp(self):
        self.widget = 'The widget'

    def tearDown(self):
        self.widget = None

    def test_foo_1(self):
        result = foo_1.print_foo_1()
        self.assertEqual(result, 'foo 1')
        self.assertEqual(self.widget, 'The widget')
        