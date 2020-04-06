import unittest

from bar import bar_1


class TestBar1(unittest.TestCase):

    def test_bar_1(self):
        result = bar_1.print_bar_1()
        self.assertEqual(result, 'bar 1')
        