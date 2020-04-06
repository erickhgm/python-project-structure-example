import unittest

from bar import bar_2


class TestBar2(unittest.TestCase):

    def test_bar_2(self):
        result = bar_2.print_bar_2()
        self.assertEqual(result, 'bar 2')
        