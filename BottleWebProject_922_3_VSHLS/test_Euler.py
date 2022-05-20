import unittest
from routes import function_transformation
class Test_test_Euler(unittest.TestCase):
    
    def test_T(self):
        matrix_correct_input = ["1;1;1","01;01;01","10;11","11;11","1;001","0","1",
                                "11111111111111","1111111111111111111111111111",
                                "11111111111111111111111111111111111111111111111111"+
                                "11111111111111111111111111111111111111111111111111",
                                "             1"]
        matrix_correct_output = ["Graph with 3 nodes and 2 edges",
                                 "Graph with 3 nodes and 2 edges",
                                 "Graph with 2 nodes and 1 edges",
                                 "Graph with 2 nodes and 1 edges",
                                 "Graph with 3 nodes and 1 edges",
                                 "Graph with 1 nodes and 0 edges",
                                 "Graph with 1 nodes and 0 edges",
                                 "Graph with 14 nodes and 13 edges",
                                 "Graph with 28 nodes and 27 edges", 
                                 "Graph with 100 nodes and 99 edges",
                                 "Graph with 1 nodes and 0 edges"]
        for i in range(len(matrix_correct_input)):
            self.assertEqual(str(function_transformation(matrix_correct_input[i])),matrix_correct_output[i]);
if __name__ == '__main__':
    unittest.main()
