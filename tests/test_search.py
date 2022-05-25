import unittest
from ch2.binary_search import binary_search
from ch2.linear_search import linear_search


class TestLinearSearch(unittest.TestCase):
    def test_linear_search_target_within_range(self):
        A = [1, 22, 34, 35, 36, 99, 101]
        
        v = 1
        self.assertEqual(linear_search(A, v), 0)

        v = 101
        self.assertEqual(linear_search(A, v), 6)

        v = 22
        self.assertEqual(linear_search(A, v), 1)

        v = 23
        self.assertIsNone(linear_search(A, v))


    def test_linear_search_target_out_of_range(self):
        A = [1, 22, 34, 35, 36, 99, 101]
        
        v = 102
        self.assertIsNone(linear_search(A, v))

        v = 0
        self.assertIsNone(linear_search(A, v))
        
class TestBinarySearch(unittest.TestCase):
    def test_binary_search_target_within_range(self):
        A = [1, 22, 34, 35, 36, 99, 101]
        
        v = 1
        self.assertEqual(binary_search(A, v), 0)

        v = 101
        self.assertEqual(binary_search(A, v), 6)

        v = 22
        self.assertEqual(binary_search(A, v), 1)

        v = 23
        self.assertIsNone(binary_search(A, v))

    def test_binary_search_target_out_of_range(self):
        A = [1, 22, 34, 35, 36, 99, 101]
        
        v = 102
        self.assertIsNone(binary_search(A, v))

        v = 0
        self.assertIsNone(binary_search(A, v))


if __name__ == "__main__":
    unittest.main()
