import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_init(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(12)
        self.assertEqual(base3.id, 12)
        base4 = Base()
        self.assertEqual(base4.id, 3)


if __name__ == '__main__':
    unittest.main()
