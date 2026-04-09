import unittest
from app import  divide_numbers


class TestApp(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide_numbers(10, 2), 5)


if __name__ == "__main__":
    unittest.main()
