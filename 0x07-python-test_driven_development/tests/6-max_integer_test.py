"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A unit test case for the `max_integer` function.
    """

    def test__max_integer__empty_list__return_none(self):
        """
        Test the behavior of `max_integer` when an empty list is passed.
        It verifies that the function returns None.
        """
        self.assertIsNone(max_integer([]))

    def test__max_integer__None_input__return_none(self):
        """
        Test the behavior of `max_integer` when None is passed as input.
        It verifies that the function raises a TypeError.
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test__max_integer__list_numeric_values__return_max_num(self):
        """
        Test the behavior of `max_integer`
            when a list of numeric values is passed.
        It verifies that the function returns
            the maximum numeric value from the list.
        """
        self.assertEqual(max_integer([2, 3, 4]), 4)
        self.assertEqual(max_integer([11, 9, 8]), 11)
        self.assertEqual(max_integer([5, 8, 2]), 8)

    def test__max_integer__list_char_and_string_values__return_max_char(self):
        """
        Test the behavior of `max_integer`
            when a list of character and string values is passed.
        It verifies that the function returns
            the maximum character or string value from the list.
        """
        self.assertEqual(max_integer(['yousef', 'ahmed', 'hassan']), 'yousef')
        self.assertEqual(max_integer(['d', 'w', 'b']), 'w')

    def test__max_integer__list_char_and_nums__raise_value_error(self):
        """
        Test the behavior of `max_integer`
            when a list containing a combination of characters,
        numbers, and dictionaries is passed.
            It verifies that the function raises a TypeError or KeyError.
        """
        with self.assertRaises(TypeError):
            max_integer(['yousef', 3, 'hassan'])

        with self.assertRaises(KeyError):
            max_integer({1: 'a', 2: 'b', 3: 'c'})


if __name__ == '__main__':
    unittest.main()
