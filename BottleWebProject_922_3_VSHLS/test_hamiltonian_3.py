import unittest
import routes
import numpy as np

#unittest for method finding Hamiltonian cycle with incorrect medium data set 
class Test_test_hamiltonian_3(unittest.TestCase):
    def test_A(self):
        non_hamiltonian_matrix = ["101;010;100", "101;010;101", "01;01", "010;011;000",
                                  "011;100;100", "000;111;100", "000;000;000", "011;000;1000",
                                  "0101;0001;0001", "1000;0010;0001", "10001;0001;1000",
                                  "0001;1000;1000", "10000;010101;10010", "1001;0001;0011", "111;000;111",
                                  "011;001;001", "010;000;100", "000;100;000", "000;100;010", "00;00",
                                  "010;000;000", "11;00", "1110;0001;1001;0001", "0111;0011;0001;0000",
                                  "0001;0000;0000;0000", "0101;0101;0101;0101", "1001;0101;0001;1000",
                                  "01000;00000;10000;01101;10000", "10;01", "001;000;111",
                                  "000;110;001", "010;100;011", "000;100;110", "0001;1000;1000;0011",
                                  "10100;00110;10000;01000;11001", "01000;10000;10000;10000;10000",
                                  "1011;0001;1000;1100"]
        for matrix in non_hamiltonian_matrix:      
            path = routes.Hamilton(routes.str_to_arr(matrix), np.empty(len(routes.str_to_arr(matrix)),dtype=int))
            self.assertEqual(path.hamiltonianCycle(), "No hamiltonian cycle for that graph!")

if __name__ == '__main__':
    unittest.main()
