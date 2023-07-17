import os
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
        base = Base((1, ))
        self.assertEqual(base.id, (1, ))

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

    
    
if __name__ == '__main__':
    unittest.main()
