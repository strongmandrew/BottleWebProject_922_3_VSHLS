import unittest
import routes

class Test_test_strongmandrew_1(unittest.TestCase):
    def test_A(self):
        correct_matrix = ["111;111;111","01;01", "101;100;000", "000;010;111", "11100;00111", "10101;011110;0010;111001"
                          , "01001;0010;00011;01010;01001", "01;00", "01001;100110;01010;010", "0100100;010110;00", "010101;01"
                          , "10011;01001;1001;1110", "00101;100;1110;1001", "01001;101010", "00;11", "10100111;01001011"
                          , "010010;111000;010", "11111;11111;11111;11111;11111", "0100;1000", "00000;00000", "01010011;10"
                          , "1001010;00010", "01001;100000", "001010;0101111", "00101;01010", "10001;00", "11010010", "0100;100",
                          "0000101;100000", "1000010;010010101", "101010;01010", "010101010;1000", "01010010;001010", "001010;01",
                          "01010011;01010010", "01001;11", "01010;01", "01001;10000;010011;0000111", "10000;0001111",
                          "0000110;110000;01;10", "010100001;10000111", "010101010;00011;1000;1000;00", "00101011;1010011;00",
                          "000111;1000;00111", ";101000;111", "0111;10000;100;0100", "1010011", "101011;11111", "0100111;11", 
                          "1000111;10001;001;1111", "0111110;1110;0100111", "010000101;0101;1001", "010000001001;010;111",
                          "001001010;0101001111", "001001111;001111000111", "0010100;0111;100111"]
        for matrix in correct_matrix:
            self.assertTrue(routes.isMatrix(matrix))

if __name__ == '__main__':
    unittest.main()
