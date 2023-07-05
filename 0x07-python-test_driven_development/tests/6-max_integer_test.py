"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A unit test case for the `max_integer` function.
    """

    def test__max_integer__empty_list__return_none(self):
        """test__max_integer__empty_list__return_none"""
        self.assertIsNone(max_integer([]))

    def test__max_integer__None_input__return_none(self):
        """test__max_integer__None_input__return_none"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test__max_integer__list_numeric_values__return_max_num(self):
        """test__max_integer__list_numeric_values__return_max_num"""
        self.assertEqual(max_integer([2, 3, 4]), 4)

    def test__max_integer__list_numeric_values1__return_max_num(self):
        """test__max_integer__list_numeric_values1__return_max_num"""
        self.assertEqual(max_integer([11, 9, 8]), 11)

    def test__max_integer__list_numeric_values2__return_max_num(self):
        """test__max_integer__list_numeric_values2__return_max_num"""
        self.assertEqual(max_integer([5, 8, 2]), 8)

    def test__max_integer__list_of_string_values__return_max_char(self):
        """test__max_integer__list_of_string_values__return_max_char"""
        self.assertEqual(
            max_integer(['yousef', 'ahmed', 'hassan']), 'yousef'
        )

    def test__max_integer__list_char_values__return_max_char(self):
        """test__max_integer__list_char_values__return_max_char"""
        self.assertEqual(max_integer(['d', 'w', 'b']), 'w')

    def test__max_integer__list_char_and_nums__raise_value_error(self):
        """test__max_integer__list_char_and_nums__raise_value_error"""
        with self.assertRaises(TypeError):
            max_integer(['yousef', 3, 'hassan'])

    def test__max_integer__dict_char_and_nums__raise_key_error(self):
        """test__max_integer__dict_char_and_nums__raise_key_error"""
        with self.assertRaises(KeyError):
            max_integer({1: 'a', 2: 'b', 3: 'c'})

    def test__max_integer__list_one_element__raise_value_error(self):
        """test__max_integer__list_one_element__raise_value_error"""
        self.assertEqual(max_integer([6]), 6)

    def test__max_integer__list_ints_and_floats__raise_value_error(self):
        """test__max_integer__list_ints_and_floats__raise_value_error"""
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)

    def test__max_integer__list_empty_string__raise_value_error(self):
        """test__max_integer__list_empty_string__raise_value_error"""
        self.assertIsNone(max_integer(""))

    def test__max_integer__one_string__raise_value_error(self):
        """test__max_integer__one_string__raise_value_error"""
        self.assertEqual(max_integer('yousef'), 'y')

    def test__max_integer__list_of_floats__raise_value_error(self):
        """test__max_integer__list_of_floats__raise_value_error"""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)


if __name__ == '__main__':
    unittest.main()
