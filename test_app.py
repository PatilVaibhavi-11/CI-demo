import unittest
from app import  divide_number


class TestApp(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide_number(10, 2), 5)


if __name__ == "__main__":
    unittest.main()
