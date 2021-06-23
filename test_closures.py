"""
Test Cases for the closures.py functions
Author: Shilpaj Bhalerao
Date: Jun 19, 2021
"""
# Standard Library Imports
import math
import types
from time import perf_counter
from unittest import TestCase

# Local Imports
from closures import docstring_checker, fib_generator, function_call_counter, COUNTER, function_call_counter_, _add, _mul, _div


def some_function_without_docstring():
    pass


def some_function_without_content():
    """

    """
    return None


class TestDocstring(TestCase):
    """
    Test Cases for Closure with docstring checking capabilities
    """
    def test_docstring_checker_add(self):
        """
        Test case for the function `_add()` which has docstring of more than 50 characters
        """
        doc_str = _add.__doc__
        doc_str = "".join(doc_str.split())
        print(f'Docstring of _add function without spaces: {doc_str}')
        print(f'Length of docstring of _add function: {len(doc_str)}')

        func = docstring_checker(_add, threshold=50)
        print(f'Threshold: {50}    Docstring Length: {len(doc_str)}    Closure returned: {func()}')
        self.assertTrue(func())

    def test_docstring_checker_perf_counter(self):
        """
        Test case for the function `perf_counter` which has docstring of less than 100 characters
        """
        doc_str = perf_counter.__doc__
        doc_str = "".join(doc_str.split())
        print(f'Docstring of perf_counter function without spaces: {doc_str}')
        print(f'Length of docstring of perf_counter function: {len(doc_str)}')

        func = docstring_checker(perf_counter, threshold=100)
        print(f'Threshold: {100}    Docstring Length: {len(doc_str)}    Closure returned: {func()}')
        self.assertFalse(func())

    def test_docstring_checker_no_docstring(self):
        """
        Test case for a function without docstring named `some_function_without_docstring`
        """
        doc_str = some_function_without_docstring.__doc__
        print(f'Docstring of some_function_without_docstring function without spaces: {doc_str}')

        func = docstring_checker(some_function_without_docstring, threshold=50)
        print(f'Threshold: {50}    Docstring Length: 0    Closure returned: {func()}')
        self.assertFalse(func())

    def test_docstring_checker_no_docstring_content(self):
        """
        Test case for a function without docstring named `some_function_without_content`
        """
        doc_str = some_function_without_content.__doc__
        doc_str = "".join(doc_str.split())
        print(f'Docstring of some_function_without_content function without spaces: {doc_str}')
        print(f'Length of docstring of some_function_without_content function: {len(doc_str)}')

        func = docstring_checker(some_function_without_content, threshold=50)
        print(f'Threshold: {50}    Docstring Length:  {len(doc_str)}    Closure returned: {func()}')
        self.assertFalse(func())


class TestFibGen(TestCase):
    """
    Test Cases for Fibonacci Series generating Closure
    """
    def setUp(self) -> None:
        """
        Initialize Variables needed for the testing
        """
        self.fib_10 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    def test_fib_10_digits(self):
        """
        Test case to check if first 10 digits of Fibonacci series are printed correctly
        """
        result = []
        func = fib_generator()
        for i in range(10):
            result.append(func())

        print(f'True Values: {self.fib_10}')
        print(f'Generated Values: {result}')
        self.assertEqual(self.fib_10, result)

    def test_fib_third_element(self):
        """
        Test case to check if the 3rd element of Fibonacci series is correct
        """
        func = fib_generator()
        print(f"First Element: {func()}")
        print(f"Second Element: {func()}")
        self.assertEqual(2, func())

    def tearDown(self) -> None:
        """
        Destructor for the testing variables
        """
        del self.fib_10


class TestCounterClosure(TestCase):
    """
    Test Cases for the function call counter
    """
    def setUp(self) -> None:
        """
        Initialize variables for Counter Closure
        """
        self.acceptable_add_data = [int(), str(), float(), list(), tuple(), dict()]
        self.unacceptable_add_data = [None, math.nan, math.inf, -math.inf]

    def test_call_counter_add_acceptable_data(self):
        """
        Test Case to check if dictionary return correct number of calls for _add function
        """
        acceptable_data = [(0, 1), (0.5, 6.21), ((1, 2), (3, 4)), ([5, 6], [7, 8]), (1+2j, 3-5j),
                           (math.nan, math.nan), (math.inf, -math.inf)]
        func = function_call_counter(_add)
        for i in acceptable_data:
            func(i[0], i[1])
        self.assertEqual(len(acceptable_data), COUNTER['_add'])

    def test_call_counter_add_unacceptable_data(self):
        """
        Test Case to check if dictionary return correct number of calls for _add function for the unacceptable inputs
        """
        count = 0
        unacceptable_data = [(None, None), ("some_string", 1), ("some_string", 2.0), (None, 'some_string'), (None, 2)]
        func = function_call_counter(_add)
        for i in unacceptable_data:
            try:
                func(i[0], i[1])
            except Exception:
                count += 1
                print("Exception Caught")
                self.assertRaises(Exception)
        self.assertEqual(len(unacceptable_data), COUNTER['_add'])
        self.assertEqual(count, len(unacceptable_data))

    def test_call_counter_mul_acceptable_data(self):
        """
        Test case to check the correct counter update with acceptable datatype for _mul function
        """
        acceptable_data = [(0, 1), (0.5, 6.21), (1+2j, 3-5j), ("some_string", 2), (math.nan, math.nan), (math.inf, -math.inf)]
        func = function_call_counter(_mul)
        for i in acceptable_data:
            func(i[0], i[1])
        self.assertEqual(len(acceptable_data), COUNTER['_mul'])

    def test_call_counter_mul_unacceptable_data(self):
        """
        Test case to check the correct counter update with unacceptable datatype for _mul function
        """
        count = 0
        unacceptable_data = [(None, None), ((1, 2), (3, 4)), ([5, 6], [7, 8]), (None, 'some_string'), (None, 2)]
        func = function_call_counter(_mul)
        for i in unacceptable_data:
            try:
                func(i[0], i[1])
            except Exception:
                count += 1
                print("Exception Caught")
                self.assertRaises(Exception)
        self.assertEqual(len(unacceptable_data), COUNTER['_mul'])
        self.assertEqual(count, len(unacceptable_data))

    def test_call_counter_div_acceptable_data(self):
        """
        Test case to check the correct counter update with acceptable datatype for `_div` function
        """
        acceptable_data = [(0, 1), (0.5, 6.21), (1+2j, 3-5j), (math.nan, math.nan), (math.inf, -math.inf)]
        func = function_call_counter(_div)
        for i in acceptable_data:
            result = func(i[0], i[1])
            print(result)
        self.assertEqual(len(acceptable_data), COUNTER['_div'])

    def test_call_counter_div_unacceptable_data(self):
        """
        Test case to check the correct counter update with unacceptable datatype for `_div` function
        """
        count = 0
        unacceptable_data = [(1, 0), (None, None), ("some_string", 2), ((1, 2), (3, 4)), ([5, 6], [7, 8]), (None, 'some_string'), (None, 2)]
        func = function_call_counter(_div)
        for i in unacceptable_data:
            try:
                func(i[0], i[1])
            except Exception:
                count += 1
                print("Exception Caught")
                self.assertRaises(Exception)
        self.assertEqual(len(unacceptable_data), COUNTER['_div'])
        self.assertEqual(count, len(unacceptable_data))

    def test_docstring(self):
        """
        Test Case to check if docstring is present in the function counter
        """
        doc_str_outer = function_call_counter.__doc__
        self.assertGreater(len(doc_str_outer), 50)

    def test_output_of_outer_and_inner(self):
        """
        Test Case to check the output of the inner and outer function of the closure
        """
        func = function_call_counter(_add)
        self.assertIsInstance(func, types.FunctionType)


class TestModifiedCounter(TestCase):
    """
    Test Cases to show individual dictionary call count is increased even when error is raised
    """
    def setUp(self) -> None:
        """

        """
        self._test_data = [(1, 2.5), (2, "Hello"), (1 + 2j, 2 + 2j), (None, None), (math.nan, math.nan), (math.inf, math.inf), ((1, 2), (2, 3)), ([5, 7], [8, 9])]

    def test_dictionary(self):
        """
        Test if dictionary is passed or not
        """
        add_dict = dict()
        mul_dict = dict()
        div_dict = dict()
        counted_add = function_call_counter_(_add, add_dict)
        counted_mul = function_call_counter_(_mul, mul_dict)
        counted_div = function_call_counter_(_div, div_dict)

        list1 = range(10)
        list2 = range(11, 21)
        for ele1, ele2 in zip(list1, list2):
            counted_add(ele1, ele2)
            counted_mul(ele1, ele2)
            counted_div(ele1, ele2)
        self.assertEqual(len(list1), add_dict['_add'])
        self.assertEqual(len(list1), mul_dict['_mul'])
        self.assertEqual(len(list1), div_dict['_div'])

    def test_counter_add(self):
        """
        Check if the dictionary is updated properly for the `_add` function
        """
        add_dict = dict()
        counted_add = function_call_counter_(_add, add_dict)

        for i in self._test_data:
            try:
                result = counted_add(i[0], i[1])
                self.assertTrue(result)
                print("Result: ", result)
            except Exception as error:
                print("Error Raised: ", error)
                self.assertRaises(Exception)

    def test_counter_mul(self):
        """
        Check if the dictionary is updated properly for the `_mul` function
        """
        mul_dict = dict()
        counted_mul = function_call_counter_(_mul, mul_dict)

        for i in self._test_data:
            try:
                result = counted_mul(i[0], i[1])
                self.assertTrue(result)
                print("Result: ", result)
            except Exception as error:
                print("Error Raised: ", error)
                self.assertRaises(Exception)

    def test_counter_div(self):
        """
        Check if the dictionary is updated properly for the `_div` function
        """
        div_dict = dict()
        counted_div = function_call_counter_(_div, div_dict)

        for i in self._test_data:
            try:
                result = counted_div(i[0], i[1])
                self.assertTrue(result)
                print("Result: ", result)
            except Exception as error:
                print("Error Raised: ", error)
                self.assertRaises(Exception)

    def test_docstring(self):
        """
        Check if docstring is present for the closure functions
        """
        div_dict = dict()
        counted_div = function_call_counter_(_div, div_dict)
        doc_str = counted_div.__doc__
        self.assertGreaterEqual(len(doc_str), 50)

    def test_output_of_outer_and_inner(self):
        """
        Test case to check the output of the `outer` and `inner` function are valid
        """
        add_dict = dict()
        counted_add = function_call_counter_(_add, add_dict)

        list1 = list(range(10))
        list2 = list(range(11, 21))
        for ele1, ele2 in zip(list1, list2):
            result = counted_add(ele1, ele2)
            self.assertIsInstance(counted_add, types.FunctionType)
            self.assertIsInstance(result, int)
