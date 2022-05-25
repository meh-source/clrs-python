import unittest
from ch2.binary_addition import binary_addition


class TestBinaryAddition(unittest.TestCase):
    def test_binary_addition(self):
        A, B = [0], [0]; n = len(A)
        self.assertListEqual(binary_addition(A, B, n), [0, 0] )

        A, B = [0, 0], [1, 0]; n = len(A)
        self.assertListEqual(binary_addition(A, B, 2), [0, 1, 0])

        A, B = [1, 0], [1, 0]; n = len(A)
        self.assertListEqual(binary_addition(A, B, 2), [1, 0, 0])


if __name__ == "__main__":
    unittest.main()
