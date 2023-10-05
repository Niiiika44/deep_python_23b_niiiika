from io import StringIO
from time import sleep
import unittest
from unittest import mock

from src.second_timer_decorator import mean


class TestFirst(unittest.TestCase):
    def setUp(self):
        self.func = lambda x: sleep(x)

    def test_time_wrong_type(self):
        with self.assertRaises(TypeError):
            self.func = mean('abc')(self.func)(2)

    def test_zero_or_negative_time(self):
        with self.assertRaises(ValueError):
            self.func = mean(-1)(self.func)(2)

        with self.assertRaises(ValueError):
            self.func = mean(0)(self.func)(2)

    def test_callable_func(self):
        with self.assertRaises(TypeError):
            self.func = mean(1)(1)(1)

    def test_decorator_output_type(self):
        self.func = mean(1)(self.func)
        self.assertTrue(callable(self.func))

    def test_decorator_output_single(self):
        with mock.patch('sys.stdout', new=StringIO())\
              as mock_out:
            mean(1)(self.func)(1)
            expected_out = 'The average execution time for 1 '\
                'recent calls is 1 seconds.\n'
        self.assertEqual(mock_out.getvalue(), expected_out)

    def test_decorator_output_multiple(self):
        with mock.patch('sys.stdout', new=StringIO())\
              as mock_out:
            mean(1)(self.func)(1)
            mean(1)(self.func)(2)
            expected_out = 'The average execution time for 1 '\
                'recent calls is 1 seconds.\n'
            expected_out += 'The average execution time for 1 '\
                'recent calls is 2 seconds.\n'
        self.assertEqual(mock_out.getvalue(), expected_out)

    def test_decorator_output_average(self):
        with mock.patch('sys.stdout', new=StringIO())\
              as mock_out:
            self.func = mean(2)(self.func)
            self.func(2)
            self.func(8)
            expected_out = 'The average execution time for 2 '\
                'recent calls is 2 seconds.\n'
            expected_out += 'The average execution time for 2 '\
                'recent calls is 5 seconds.\n'
        self.assertEqual(mock_out.getvalue(), expected_out)

    def test_decorator_output_multiple_related(self):
        with mock.patch('sys.stdout', new=StringIO())\
              as mock_out:
            self.func = mean(1)(self.func)
            self.func(1)
            self.func(2)
            expected_out = 'The average execution time for 1 '\
                'recent calls is 1 seconds.\n'
            expected_out += 'The average execution time for 1 '\
                'recent calls is 2 seconds.\n'
        self.assertEqual(mock_out.getvalue(), expected_out)

    def test_correctness_average_time(self):
        with mock.patch('sys.stdout', new=StringIO())\
              as mock_out:
            self.func = mean(3)(self.func)
            self.func(1)
            self.func(3)
            self.func(3)
            self.func(3)
            self.func(6)
            expected_out = 'The average execution time for 3 '\
                'recent calls is 1 seconds.\n'
            expected_out += 'The average execution time for 3 '\
                'recent calls is 2 seconds.\n'
            expected_out += 'The average execution time for 3 '\
                'recent calls is 2 seconds.\n'
            expected_out += 'The average execution time for 3 '\
                'recent calls is 3 seconds.\n'
            expected_out += 'The average execution time for 3 '\
                'recent calls is 4 seconds.\n'
        self.assertEqual(mock_out.getvalue(), expected_out)

    def test_func_immutability(self):
        func = lambda x: x
        func_decorated = mean(3)(func)
        func_decorated(2)
        self.assertEqual(func(2), func_decorated(2))
