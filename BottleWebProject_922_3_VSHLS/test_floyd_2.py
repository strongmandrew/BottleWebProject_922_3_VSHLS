import unittest
from routes import Floydclone
class Test_test_floyd_2(unittest.TestCase):
    def test_A(self):
        str1 = "43,12,23,43"
        eq = "{'1': {'1': 0, '4': 1.0, '2': 1.0, '3': 2.0}, '4': {'4': 0, '1': 1.0, '3': 1.0, '2': 2.0}, '2': {'2': 0, '1': 1.0, '3': 1.0, '4': 2.0}, '3': {'3': 0, '4': 1.0, '2': 1.0, '1': 2.0}}"
        self.assertEqual(Floydclone(str1),eq)

if __name__ == '__main__':
    unittest.main()
