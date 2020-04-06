import unittest

from foo import foo_2


class TestBar2(unittest.TestCase):

    def test_foo_2(self):
        result = foo_2.print_foo_2()
        self.assertEqual(result, 'foo 2')
