import unittest
from unittest import mock

import main


class TestMain(unittest.TestCase):

    @mock.patch('main.foo_2', autospec=True)
    @mock.patch('main.foo_1', autospec=True)
    @mock.patch('main.bar_2', autospec=True)
    @mock.patch('main.bar_1', autospec=True)
    def test_main(self, mock_bar_1, mock_bar_2, mock_foo_1, mock_foo_2):
        mock_bar_1.print_bar_1.return_value = 'mock_bar_1'
        mock_bar_2.print_bar_2.return_value = 'mock_bar_2'
        mock_foo_1.print_foo_1.return_value = 'mock_foo_1'
        mock_foo_2.print_foo_2.return_value = 'mock_foo_2'

        main.main()

        self.assertTrue(mock_bar_1.print_bar_1.called, "Failed, bar_1.print_bar_1 method not called.")
        self.assertTrue(mock_bar_2.print_bar_2.called, "Failed, bar_2.print_bar_1 method not called.")
        self.assertTrue(mock_foo_1.print_foo_1.called, "Failed, foo_1.print_foo_2 method not called.")
        self.assertTrue(mock_foo_2.print_foo_2.called, "Failed, foo_2.print_foo_2 method not called.")
