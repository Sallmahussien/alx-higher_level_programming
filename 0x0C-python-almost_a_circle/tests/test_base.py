import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):

    def test_base_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)

    def test_base_with_none(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base2.id, base1.id + 1)

    def test_base_with_int(self):
        base = Base(12)
        self.assertEqual(base.id, 12)

    def test_base_with_str(self):
        base = Base('str')
        self.assertEqual(base.id, 'str')

    def test_base_with_float(self):
        base = Base(3.1)
        self.assertEqual(base.id, 3.1)

    def test_base_with_list(self):
        base = Base([1, 2, 3])
        self.assertEqual(base.id, [1, 2, 3])

    def test_base_with_tuple(self):
        base = Base((1,))
        self.assertEqual(base.id, (1,))

    def test_base_with_set(self):
        base = Base({1, 2})
        self.assertEqual(base.id, {1, 2})

    def test_base_with_dict(self):
        base = Base({'a': 1, 'b': 2})
        self.assertEqual(base.id, {'a': 1, 'b': 2})

    def test_base_with_bool(self):
        base = Base(False)
        self.assertEqual(base.id, False)

    def test_base_with_neg_int(self):
        base = Base(-1)
        self.assertEqual(base.id, -1)

    def test_base_with_zero(self):
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_base_with_cmplx_num(self):
        base = Base(complex(5, 7))
        self.assertEqual(base.id, complex(5, 7))

    def test_base_with_INF(self):
        base = Base(float('inf'))
        self.assertEqual(base.id, float('inf'))

    def test_base_with_neg_INF(self):
        base = Base(float('-inf'))
        self.assertEqual(base.id, float('-inf'))

    def test_base_with_large_num(self):
        base = Base(999999999999999999999999999999)
        self.assertEqual(base.id, 999999999999999999999999999999)

    def test_base_with_NAN(self):
        base = Base(float('nan'))
        self.assertNotEqual(base.id, float('nan'))

    def test_base_with_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Unittests of to_json_string of Base class"""

    def test_to_json_string_with_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_with_None(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_with_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list_of_dict(self):
        dict_list = [{"a": 5, "b": 10}, {"c": 1, "d": 2}]
        expected_str = "[{\"a\": 5, \"b\": 10}, {\"c\": 1, \"d\": 2}]"
        self.assertEqual(Base.to_json_string(dict_list), expected_str)

    def test_to_json_string_list_tuple(self):
        dict_list_of_tuple = [(5, 10), (1, 2)]
        expected_str = """[[5, 10], [1, 2]]"""
        self.assertEqual(Base.to_json_string(dict_list_of_tuple), expected_str)

    def test_to_json_string_list_set(self):
        dict_list_of_set = [(5, 10), {1, 2}]
        with self.assertRaises(TypeError):
            Base.to_json_string(dict_list_of_set)

    def test_to_json_string_list_to_dict_rect(self):
        r = Rectangle(10, 7, 2, 8, 7)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_str = """[{"id": 7, "width": 10, "height": 7, "x": 2, "y": 8}]"""
        self.assertEqual(json_dictionary, expected_str)

    def test_to_json_string_list_to_dict_square(self):
        s = Square(5, 1, 2, 8)
        dictionary = s.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_str = """[{"id": 8, "size": 5, "x": 1, "y": 2}]"""
        self.assertEqual(json_dictionary, expected_str)

    def test_to_json_with_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string(1, 2)


class TestBaseFromJsonString(unittest.TestCase):

    def test_from_json_string_with_no_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_with_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_with_empty_list(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_list_of_dict(self):
        json_list = "[{\"a\": 5, \"b\": 10}, {\"c\": 1, \"d\": 2}]"
        expected_list = [{"a": 5, "b": 10}, {"c": 1, "d": 2}]
        self.assertEqual(Base.from_json_string(json_list), expected_list)

    def test_from_json_string_list_of_list(self):
        json_list = """[[5, 10], [1, 2]]"""
        expected_list = [[5, 10], [1, 2]]
        self.assertEqual(Base.from_json_string(json_list), expected_list)

    def test_from_json_string_list_to_dict_rect(self):
        r = Rectangle(10, 7, 2, 8, 1)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(Base.from_json_string(json_dictionary), [dictionary])

    def test_from_json_string_list_to_dict_square(self):
        s = Square(5, 1, 2, 8)
        dictionary = s.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(Base.from_json_string(json_dictionary), [dictionary])

    def test_from_json_with_two_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(1, 2)


if __name__ == '__main__':
    unittest.main()
