import unittest
from routes import funcEulerCloneForUT

class Test_test_Euler_two(unittest.TestCase):

    def test_A(self):
        matrix_Euler_graphs_input = ["111;111;111","01;001;1","001;1;01;","1","11;011;1","0", "             1"]
        matrix_Euler_graphs_output = ["Graph is Euler (1, 3) -> (3, 3) -> (3, 2) -> (2, 2) -> (2, 3) -> (3, 1) -> (1, 2) -> (2, 1) -> (1, 1)",
                                  "Graph is Euler (1, 2) -> (2, 3) -> (3, 1)", 
                                  "Graph is Euler (1, 3) -> (3, 2) -> (2, 1)",
                                  "Graph is Euler (1, 1)",
                                  "Graph is Euler (1, 2) -> (2, 2) -> (2, 3) -> (3, 1) -> (1, 1)",
                                  "Graph is Euler ", "Graph is Euler (1, 1)"]
        for i in range(len(matrix_Euler_graphs_input)):
            self.assertEqual(str(funcEulerCloneForUT(matrix_Euler_graphs_input[i])),matrix_Euler_graphs_output[i]);

    def test_B(self):
        matrix_notEuler_graphs_input = ["11","111","1111111111111","11111;1","0;0","0;1;0;1;01;011"]
        matrix_notEuler_graphs_output = "Graph is not Euler"
        for i in range(len(matrix_notEuler_graphs_input)):
            self.assertEqual(str(funcEulerCloneForUT(matrix_notEuler_graphs_input[i])),matrix_notEuler_graphs_output);

    def test_C(self):
        matrix_uncorrect_input = ["","2","3","4","5","6;1;0","\01","`1","^\d$","(01;1)","01;1,2"]
        matrix_uncorrect_output = "Doesn't match the pattern of matrix"
        for i in range(len(matrix_uncorrect_input)):
            self.assertEqual(str(funcEulerCloneForUT(matrix_uncorrect_input[i])),matrix_uncorrect_output);

if __name__ == '__main__':
    unittest.main()
