import timeit
import unittest

from reducers.common_reducers import *

class AllMaxReducerTests(unittest.TestCase):

    def test_all(self):
        test_input = [1, 2, 3, 4]
        answer = 4
        self.assertEqual(for_loop_max(test_input), answer)
        self.assertEqual(reducer_max(test_input), answer)
        self.assertEqual(argument_list_max(test_input), answer)
        self.assertEqual(reducer_passed_in(test_input), answer)
        self.assertEqual(reducer_with_lambda(test_input), answer)

class BenchmarkReducers(unittest.TestCase):

    def setUp(self):
        LIST_SIZE = 10000
        self.test_input_list = [i for i in range(LIST_SIZE)]
        self.test_input_iterable = range(LIST_SIZE)
        self.num_iters = 1000
        print("Benchmarking")

    def test_for_loop_max(self):
        print("for_loop_max")
        env = globals()
        env["self"] = self
        t = timeit.Timer("for_loop_max(self.test_input_list)", globals=env)
        print(t.timeit(self.num_iters))
        t = timeit.Timer("for_loop_max(self.test_input_iterable)", globals=env)
        print(t.timeit(self.num_iters))

    def test_reducer_max(self):
        print("reducer_max")
        env = globals()
        env["self"] = self
        t = timeit.Timer("reducer_max(self.test_input_list)", globals=env)
        print(t.timeit(self.num_iters))
        t = timeit.Timer("reducer_max(self.test_input_iterable)", globals=env)
        print(t.timeit(self.num_iters))

    def test_argument_list_max(self):
        print("argument_list_max")
        env = globals()
        env["self"] = self
        t = timeit.Timer("argument_list_max(self.test_input_list)", globals=env)
        print(t.timeit(self.num_iters))
        t = timeit.Timer("argument_list_max(self.test_input_iterable)", globals=env)
        print(t.timeit(self.num_iters))

    def test_reducer_passed_in(self):
        print("reducer_passed_in")
        env = globals()
        env["self"] = self
        t = timeit.Timer("reducer_passed_in(self.test_input_list)", globals=env)
        print(t.timeit(self.num_iters))
        t = timeit.Timer("reducer_passed_in(self.test_input_iterable)", globals=env)
        print(t.timeit(self.num_iters))

    def test_reducer_with_lambda(self):
        print("reducer_with_lambda")
        env = globals()
        env["self"] = self
        t = timeit.Timer("reducer_with_lambda(self.test_input_list)", globals=env)
        print(t.timeit(self.num_iters))
        t = timeit.Timer("reducer_with_lambda(self.test_input_iterable)", globals=env)
        print(t.timeit(self.num_iters))
