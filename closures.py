"""
Scripts containing closures
Author: Shilpaj Bhalerao
Date: Jun 19, 2021
"""
# Standard Library Imports
import operator

# Dictionaries for logging function call
COUNTER = {}


def docstring_checker(func, threshold):
    """
    Docstring checker Closure
    :param func: Input function
    :param threshold: Number of character needed in the docstring
    :return: Inner function to check the docstring content length
    """
    threshold_value = threshold

    def inner():
        """
        Inner function for the closure
        :return: Boolean True if docstring characters are greater than the `threshold`
        """
        func_docstring = func.__doc__
        if func_docstring is not None:
            func_docstring = "".join(func_docstring.split())
            if len(func_docstring) > threshold_value:
                return True
            return False
        return False
    return inner


def fib_generator():
    """
    Closure for Fibonacci series generator
    :return: Inner function which returns next fibonacci number
    """
    num1 = 1
    num2 = 1
    count = 0

    def inner():
        """
        Function to generate next Fibonacci number
        :return: Fibonacci number
        """
        nonlocal num1, num2, count
        count += 1

        if count < 3:
            return 1
        num1, num2 = num2, operator.add(num1, num2)
        return num2
    return inner


def function_call_counter(func):
    """
    Closure to count the number of times a function is called
    :param func: Function whose calls are counted
    :return: Inner function of the closure
    """
    count = 0

    def inner(*args, **kwargs):
        """
        Inner function of a closure which adds the function and it's count number to the dictionary
        :return: output of the function
        """
        nonlocal count
        global COUNTER
        count += 1
        print(f'Function {func.__name__} has been called {count} times')
        COUNTER[func.__name__] = count
        return func(*args, **kwargs)
    return inner


def function_call_counter_(func, dict_name):
    """
    Closure to count the number of times a function is called
    :param func: Function whose calls are counted
    :param dict_name: Dictionary which stores the number of time function is called
    :return: Inner function of the closure
    """
    count = 0

    def inner(*args, **kwargs):
        """
        Inner function of the closure which adds function calls to the dictionary
        :return: Output of the function called with input arguments
        """
        nonlocal count
        count += 1
        print(f'Function {func.__name__} has been called {count} times')
        dict_name[func.__name__] = count
        return func(*args, **kwargs)
    return inner


def _add(element_1, element_2):
    """
    Addition of two numbers
    :param element_1: First number
    :param element_2: Second number
    :return: Sum of above two numbers
    """
    return operator.add(element_1, element_2)


def _mul(element_1, element_2):
    """
    Addition of two numbers
    :param element_1: First number
    :param element_2: Second number
    :return: Sum of above two numbers
    """
    return operator.mul(element_1, element_2)


def _div(element_1, element_2):
    """
    Addition of two numbers
    :param element_1: First number
    :param element_2: Second number
    :return: Sum of above two numbers
    """
    return operator.truediv(element_1, element_2)
