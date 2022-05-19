import unittest
from routes import isFloyd;
class Test_test_Floyd_1(unittest.TestCase):
    def test_T(self):
        strt1 = "15,17,89,76,23,45,12,55,33,56,88,55,49,58,34,86"
        strt2 = "76,99,00"
        strt3="12,45,76"
        self.assertTrue(isFloyd(strt1))
        self.assertTrue(isFloyd(strt2))
        self.assertTrue(isFloyd(strt3))
    def test_F(self):
        strf1="11,24,567"
        strf2 = "12,45,qq"
        strf3="1,45,65"
        self.assertFalse(isFloyd(strf1))
        self.assertFalse(isFloyd(strf2))
        self.assertFalse(isFloyd(strf3))

if __name__ == '__main__':
    unittest.main()
