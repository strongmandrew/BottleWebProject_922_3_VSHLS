import unittest
from routes import function_transformation
class Test_test_Euler(unittest.TestCase):
    
    def test_T(self):
        matrix_correct_input = ["1;1;1","01;01;01","10;11","11;11","1;001","0","1",
                                "11111111111111","1111111111111111111111111111",
                                "11111111111111111111111111111111111111111111111111"+
                                "11111111111111111111111111111111111111111111111111",
                                "             1"]
        matrix_correct_output = ["DiGraph with 3 nodes and 3 edges",
                                 "DiGraph with 3 nodes and 3 edges",
                                 "DiGraph with 2 nodes and 3 edges",
                                 "DiGraph with 2 nodes and 4 edges",
                                 "DiGraph with 3 nodes and 2 edges",
                                 "DiGraph with 1 nodes and 0 edges",
                                 "DiGraph with 1 nodes and 1 edges",
                                 "DiGraph with 14 nodes and 14 edges",
                                 "DiGraph with 28 nodes and 28 edges", 
                                 "DiGraph with 100 nodes and 100 edges",
                                 "DiGraph with 1 nodes and 1 edges"]
        for i in range(len(matrix_correct_input)):
            self.assertEqual(str(function_transformation(matrix_correct_input[i])),matrix_correct_output[i]);
if __name__ == '__main__':
    unittest.main()
